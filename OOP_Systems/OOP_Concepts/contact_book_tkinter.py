import tkinter as tk
from tkinter import messagebox # Used for pop-up alerts

# ==========================================
# PART 1: YOUR LOGIC (UNCHANGED)
# ==========================================

class Contact:
    def __init__(self, name: str, phone_number: str, email=None, address=None) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def update_info(self, phone_number=None, email=None, address=None):
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address

    def get_details(self):
        # I changed display_info to return a string so the GUI can show it
        return f"M.{self.name}, living in {self.address}, phone: {self.phone_number}, email: {self.email}."

class ContactBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, name: str, phone_number: str, email=None, address=None):
        if name in self.contacts:
            return False # Return False if failed
        new_contact = Contact(name, phone_number, email, address)
        self.contacts[name] = new_contact
        return True # Return True if success

    def find_contact(self, name):
        return self.contacts.get(name, None)

    def list_all_contacts(self):
        if not self.contacts:
            return "Contact book is empty!"
        result = ""
        for contact in self.contacts.values():
            result += contact.get_details() + "\n"
        return result

# ==========================================
# PART 2: THE "REAL APP" INTERFACE (GUI)
# ==========================================

# 1. Initialize the logic
my_book = ContactBook()

# 2. Define what happens when buttons are clicked
def save_contact_action():
    # GET data from the white boxes on screen
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    addr = entry_address.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    # CALL your original logic
    success = my_book.add_contact(name, phone, email, addr)

    if success:
        messagebox.showinfo("Success", f"{name} added successfully!")
        # Clear the boxes
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_email.delete(0 ,tk.END)
    else:
        messagebox.showerror("Error", "Name already exists.")

def show_list_action():
    # CALL your original logic
    all_contacts = my_book.list_all_contacts()
    # SHOW it in a popup
    messagebox.showinfo("All Contacts", all_contacts)

# 3. Build the Window
root = tk.Tk()
root.title("My Contact Manager")
root.geometry("400x350")

# --- Create the visual elements (Widgets) ---

# Name Label and Box
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

# Phone Label and Box
tk.Label(root, text="Phone:").pack(pady=5)
entry_phone = tk.Entry(root)
entry_phone.pack()

# Email Label and Box
tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack()

# Address Label and Box
tk.Label(root, text="Address:").pack(pady=5)
entry_address = tk.Entry(root)
entry_address.pack()

# Buttons
btn_add = tk.Button(root, text="Save Contact", command=save_contact_action, bg="#4CAF50", fg="white")
btn_add.pack(pady=10)

btn_list = tk.Button(root, text="Show All Contacts", command=show_list_action)
btn_list.pack(pady=5)

# 4. Start the App Loop (This replaces 'while True')
root.mainloop()
