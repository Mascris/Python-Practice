import discord
from discord.ext import commands
import asyncio
import time

# ================= CONFIGURATION =================
# ⚠️ PASTE YOUR REAL TOKEN HERE ⚠️
TOKEN = ""

PREFIX = "$"
MOVE_INTERVAL = 1.0  
MOD_ROLES = ["Me", "[MOD]", "Admin", "Owner"] 

# Colors
COL_NEON = 0x00f7ff
COL_GREEN = 0x2ecc71
COL_RED = 0xff004c
COL_WARN = 0xffa500
COL_DARK = 0x2b2d31

# ================= SETUP =================
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# ================= HELPERS =================
def is_mod(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator: return True
    user_roles = [r.name.lower() for r in interaction.user.roles]
    allowed = [r.lower() for r in MOD_ROLES]
    return any(r in allowed for r in user_roles)

# ================= UI: CUSTOM NUMBER INPUT =================
class CustomLimitModal(discord.ui.Modal, title="Set Custom Move Limit"):
    limit_input = discord.ui.TextInput(
        label="Number of Moves",
        placeholder="e.g. 5, 20, 100...",
        min_length=1,
        max_length=4,
        required=True
    )

    def __init__(self, parent_view):
        super().__init__()
        self.parent_view = parent_view

    async def on_submit(self, interaction: discord.Interaction):
        try:
            value = int(self.limit_input.value)
            if value <= 0: raise ValueError
            self.parent_view.limit = value
            await interaction.response.send_message(f"✅ Limit set to: **{value}**", ephemeral=True)
        except ValueError:
            await interaction.response.send_message("❌ Please enter a valid positive number.", ephemeral=True)

# ================= UI: ACTIVE SHAKE MONITOR =================
class ActiveShakeView(discord.ui.View):
    def __init__(self, target, ch1, ch2, limit):
        super().__init__(timeout=None)
        self.target = target
        self.ch1 = ch1
        self.ch2 = ch2
        self.limit = limit  # 0 means infinite
        self.is_running = True
        self.count = 0
        self.start_time = time.time()

    async def run_shake(self, interaction):
        current = self.ch1
        reason = "Unknown"

        while self.is_running:
            # 1. Check if user disconnected entirely
            if not self.target.voice:
                self.is_running = False
                reason = "User Disconnected"
                break

            # 2. Check Limit (If set)
            if self.limit > 0 and self.count >= self.limit:
                self.is_running = False
                reason = "Target Limit Reached"
                break

            try:
                # 3. MOVE THE USER (Capture them from anywhere)
                await self.target.move_to(current)
                self.count += 1
                
                # Update dashboard periodically
                if self.count % 5 == 0:
                    await self.update_dashboard(interaction)

            except discord.HTTPException:
                await asyncio.sleep(2) # Rate limit protection
            except Exception as e:
                print(f"Error: {e}")
            
            # Swap target channel for next loop
            current = self.ch2 if current == self.ch1 else self.ch1
            
            # Wait for the move to process
            await asyncio.sleep(MOVE_INTERVAL)

            # 4. CHECK FOR ESCAPE (After the move/wait)
            # If the user is connected, but NOT in ch1 OR ch2, they escaped.
            if self.target.voice:
                current_channel_id = self.target.voice.channel.id
                if current_channel_id not in [self.ch1.id, self.ch2.id]:
                    self.is_running = False
                    reason = "User Escaped / Moved Away"
                    break

        # Loop finished
        await self.send_report(interaction, reason)

    async def update_dashboard(self, interaction):
        try:
            embed = interaction.message.embeds[0]
            limit_text = "Infinite" if self.limit == 0 else f"{self.limit}"
            embed.description = f"**Target:** {self.target.mention}\n**Progress:** `{self.count}` / `{limit_text}`\n**Status:** 🟢 Active"
            await interaction.message.edit(embed=embed)
        except: pass

    async def send_report(self, interaction, reason):
        duration = round(time.time() - self.start_time, 1)
        
        color = COL_GREEN if reason == "Target Limit Reached" else COL_WARN
        if reason == "Manual Stop": color = COL_RED

        embed = discord.Embed(title="📁 Mission Report", color=color)
        embed.add_field(name="Target", value=self.target.name, inline=True)
        embed.add_field(name="Total Moves", value=str(self.count), inline=True)
        embed.add_field(name="Time", value=f"{duration}s", inline=True)
        embed.add_field(name="Result", value=f"**{reason}**", inline=False)
        embed.set_footer(text="Nakhad Systems • Pro Edition")
        
        self.children[0].disabled = True
        self.children[0].label = "Ended"
        self.children[0].style = discord.ButtonStyle.secondary
        
        try:
            await interaction.message.edit(embed=embed, view=self)
        except: pass

    @discord.ui.button(label="STOP LOOP", style=discord.ButtonStyle.danger, emoji="🛑")
    async def stop_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not is_mod(interaction):
            return await interaction.response.send_message("❌ Unauthorized.", ephemeral=True)
        
        self.is_running = False
        await interaction.response.defer()
        await self.send_report(interaction, "Manual Stop")

# ================= UI: WIZARD =================
class ShakeWizard(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.selected_user = None
        self.channel_1 = None
        self.channel_2 = None
        self.limit = 0 # 0 = Infinite

    # 1. SELECT USER
    @discord.ui.select(cls=discord.ui.UserSelect, placeholder="1. Select Victim", min_values=1, max_values=1, row=0)
    async def select_user(self, interaction: discord.Interaction, select: discord.ui.UserSelect):
        user = select.values[0]
        if not user.voice:
            self.selected_user = None
            return await interaction.response.send_message(f"❌ **{user.name}** is not in a voice channel!", ephemeral=True)
        self.selected_user = user
        await interaction.response.defer()

    # 2. SELECT CHANNEL 1
    @discord.ui.select(cls=discord.ui.ChannelSelect, placeholder="2. Select Room A", channel_types=[discord.ChannelType.voice], row=1)
    async def select_ch1(self, interaction: discord.Interaction, select: discord.ui.ChannelSelect):
        self.channel_1 = select.values[0]
        await interaction.response.defer()

    # 3. SELECT CHANNEL 2
    @discord.ui.select(cls=discord.ui.ChannelSelect, placeholder="3. Select Room B", channel_types=[discord.ChannelType.voice], row=2)
    async def select_ch2(self, interaction: discord.Interaction, select: discord.ui.ChannelSelect):
        self.channel_2 = select.values[0]
        await interaction.response.defer()

    # 4. SELECT MODE (LIMIT)
    @discord.ui.select(
        placeholder="4. Select Mode (Default: Infinite)",
        options=[
            discord.SelectOption(label="Infinite Loop", value="0", description="Shake until stopped or disconnected", emoji="♾️"),
            discord.SelectOption(label="10 Moves", value="10", description="Stop after 10 moves"),
            discord.SelectOption(label="25 Moves", value="25", description="Stop after 25 moves"),
            discord.SelectOption(label="50 Moves", value="50", description="Stop after 50 moves"),
            discord.SelectOption(label="Custom Number...", value="custom", description="Type a specific number", emoji="🔢"),
        ],
        row=3
    )
    async def select_limit(self, interaction: discord.Interaction, select: discord.ui.Select):
        val = select.values[0]
        if val == "custom":
            await interaction.response.send_modal(CustomLimitModal(self))
        else:
            self.limit = int(val)
            await interaction.response.defer()

    # 5. START BUTTON
    @discord.ui.button(label="START OPERATION", style=discord.ButtonStyle.success, emoji="🚀", row=4)
    async def start_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not is_mod(interaction): return await interaction.response.send_message("❌ Unauthorized.", ephemeral=True)

        # Validation
        if not self.selected_user: return await interaction.response.send_message("❌ Missing User!", ephemeral=True)
        if not self.channel_1 or not self.channel_2: return await interaction.response.send_message("❌ Missing Channels!", ephemeral=True)
        
        # Check if user is still connected
        if not self.selected_user.voice:
            return await interaction.response.send_message("❌ User left voice before start.", ephemeral=True)

        limit_text = "Infinite" if self.limit == 0 else f"{self.limit}"

        embed = discord.Embed(title="🌪️ Shake Operation Active", color=COL_NEON)
        embed.description = f"**Target:** {self.selected_user.mention}\n**Goal:** `{limit_text}` moves\n**Status:** 🟢 Starting..."
        embed.add_field(name="Path", value=f"{self.channel_1.mention} ↔ {self.channel_2.mention}")
        embed.set_thumbnail(url=self.selected_user.avatar.url if self.selected_user.avatar else None)
        embed.set_footer(text="Nakhad Systems • Pro Edition")

        view = ActiveShakeView(self.selected_user, self.channel_1, self.channel_2, self.limit)
        await interaction.response.send_message(embed=embed, view=view)
        
        # Run background task
        asyncio.create_task(view.run_shake(interaction))

# ================= COMMANDS =================
@bot.event
async def on_ready():
    print(f"✅ Bot Online: {bot.user}")
    await bot.change_presence(activity=discord.Game(name="System Active"))

@bot.command()
async def panel(ctx):
    """Opens the main GUI"""
    embed = discord.Embed(title="🎛️ Nakhad Shake Controller", description="Configure the operation below.", color=COL_DARK)
    embed.add_field(name="Steps", value="1️⃣ Select **Victim**\n2️⃣ Select **Room A** & **Room B**\n3️⃣ Select **Limit** (Optional)\n4️⃣ Press **Start**")
    
    view = ShakeWizard()
    await ctx.send(embed=embed, view=view)

# ================= RUN =================
if __name__ == "__main__":
    if "PASTE" in TOKEN:
        print("❌ ERROR: PASTE TOKEN")
    else:
        bot.run(TOKEN)
