import re
from db import connect
from player import get_players_data 

def get_store_items():
    print("list of choice:")
    print("weapons\narmor\nall\n")
    try:

        categories = input("enter the categories of items you want to see: ").lower()
        conn = connect()
        cursor = conn.cursor()
        if categories == 'all':
            cursor.execute("SELECT * FROM STORE")
        else:
            cursor.execute("SELECT * FROM store WHERE category = %s", (categories,))
        store = cursor.fetchall()
        conn.close()
        
        if not store:
            raise ValueError("Invalid category")

        for item in store:
            print(f"Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")

    except Exception as e:
        print("⚠️ Invalid category. Please choose weapons, armor, or all.")

def buy_itemss():
    try:
        item = input("enter the name of items you want to buy: ")
        amounts = int(input(f"Enter how many pieces of '{item}' you want to buy: "))
        if amounts == 0:
            print("you should atleast buy one item")
            return

        player_id,player_coins = get_players_data(for_buy=True)
        if player_id is None:
            print("cannont proceed without selecting a valid player ID!")
            return
        
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("SELECT * from store where name=%s and quantity>=%s ",(item,amounts,))
        result = cursor.fetchone()
        cursor.execute("SELECT price from store where name=%s",(item,))
        result_price=cursor.fetchone()
        if not result:
            print("Invalid Value!")
        else:
            print(f"Name: {result[1]}, Price: {result[2]}, Quantity: {result[3]}")
            if result_price:
                item_price = result_price[0]
                total_price = item_price*amounts
                if player_coins is not None:
                    if player_coins >= total_price:
                        cursor.execute("UPDATE store set quantity = quantity-%s where player_id = %s",(total_price,player_id))
                        cursor.execute("UPDATE coins SET coins = coins-%s WHERE player_id=%s",(total_price,player_id))
                        print("you succecfully buyed the items")
                        cursor.execute("SELECT quantity from inventory where player_id = %s AND item_id=%s",(player_id,store_item_id))
                        conn.commit()
                        conn.close()
                    else:
                        print("not enought coins to buy")
                else:
                    print("you have 0 coins")
            else:
                print(f"this {item}, not found in store!")
            return result
    except ValueError:
        ("wrong")
        


def buy_items():
    try:
        item = input("enter the name of items you want to buy: ").strip().lower() # Normalize input
        amounts = int(input(f"Enter how many pieces of '{item}' you want to buy: "))
        if amounts <= 0:
            print("You should at least buy one item.")
            return

        player_id, player_coins = get_players_data(for_buy=True) 
        if player_id is None: 
            print("Cannot proceed without selecting a valid player ID!")
            return
        
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT item_id, name, price, quantity FROM store WHERE LOWER(name) = %s AND quantity >= %s", (item, amounts,))
                store_item_data = cursor.fetchone() 

                if not store_item_data:
                    print(f"Invalid item name ('{item}') or not enough quantity available in store!")
                    return 

                store_item_id = store_item_data[0] 
                store_item_name = store_item_data[1] 
                store_item_price = store_item_data[2] 

                total_price = store_item_price * amounts

                if player_coins is None or player_coins < total_price: # Check if player_coins is None or insufficient
                    print(f"Not enough coins to buy {amounts}x '{store_item_name}'. You need {total_price} coins but have {player_coins if player_coins is not None else 0}.")
                    return 

                cursor.execute("UPDATE players SET coins = coins - %s WHERE player_id = %s", (total_price, player_id))
                
                cursor.execute("UPDATE store SET quantity = quantity - %s WHERE item_id = %s", (amounts, store_item_id))

                cursor.execute("SELECT quantity FROM inventory WHERE player_id = %s AND item_id = %s", (player_id, store_item_id))
                inventory_record = cursor.fetchone()

                if inventory_record:
                    cursor.execute("UPDATE inventory SET quantity = quantity + %s WHERE player_id = %s AND item_id = %s", (amounts, player_id, store_item_id))
                else:
                    cursor.execute("INSERT INTO inventory (player_id, item_id, quantity) VALUES (%s, %s, %s)", (player_id, store_item_id, amounts))

                conn.commit() 
                print(f"🥳 You successfully bought {amounts}x '{store_item_name}' for {total_price} coins!")
                print(f"Your new balance is {player_coins - total_price} coins.")
                
        return store_item_data

    except ValueError:
        print("⚠️ Invalid input. Please ensure you enter a whole number for the amount.")
    except Exception as e:
        print(f"An unexpected error occurred during purchase. No changes were saved: {e}")
