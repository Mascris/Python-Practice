from db import connect

def get_inventory():
    try:
        player_id = int(input("please Enter the ID of Player you want to Use: "))
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory WHERE player_id=%s",(player_id,))
        inventory = cursor.fetchall()
        conn.close()
        if not inventory:
            print("inventory Empty")
        else:     
            for item in inventory:
                print(f"Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
        return inventory
    except ValueError:
        print("hello")


def add_coins():
    player_id = int(input("enter the amount you want to add: "))
    amount = int(input("please eneter the id you want: "))
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE players SET coins = coins + %s WHERE player_id = %s",(amount,player_id))
    conn.commit()
    conn.close()
    print("Succesfully Added!")
    return amount

def get_players_dataa(for_buy=False):
    print("--- List of Players ---")
    print("1: mopo")
    print("2: lassa")
    print("-----------------------")
    try:
        player_id = int(input("please Enter the ID of Player you want to see the Coins: "))
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT username,coins From players WHERE player_id = %s",(player_id,))
        result = cursor.fetchone()
        conn.close()
        if not result:
            raise ValueError("⚠️ Invalid number. Please choose either 1 or 2.")

        username, coins = result
        if not for_buy:
            print(f"username: {username}, coins: {coins}")
        return player_id,coins

    except Exception as e:
        print("⚠️ Invalid Input. Please choose either 1 or 2.")
        
def get_players_data(for_buy=False):
    print("--- List of Players ---")
    print("1: mopo")
    print("2: lassa")
    print("-----------------------")
    try:
        player_id = int(input("Please Enter the ID of the Player (1 or 2) you want to use: ")) # Clarified prompt
        
        if player_id not in [1, 2]:
            print("⚠️ Invalid Player ID. Please choose either 1 or 2.")
            return None, None 

        with connect() as conn:
            with conn.cursor() as cursor: 
                cursor.execute("SELECT username,coins From players WHERE player_id = %s", (player_id,))
                result = cursor.fetchone()

        if not result:
            print("⚠️ Player not found in the database. This should not happen for valid IDs 1 or 2.")
            return None, None 

        username, coins = result
        if not for_buy:
            print(f"\nUsername: {username}, Coins: {coins}")
        return player_id, coins 

    except ValueError: 
        print("⚠️ Invalid input. Please enter a whole number for Player ID.")
        return None, None 
    except Exception as e: 
        print(f"An unexpected error occurred while fetching player data: {e}")
        return None, None 
