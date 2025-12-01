import json

#load JSON File 
player_path = "/home/mascris/project/Python/rpg-store/player.json"
store_path = "/home/mascris/project/Python/rpg-store/store.json"

with open(store_path, "r") as f:
    store = json.load(f)

with open(player_path ,"r") as f:
    player = json.load(f)

#code 

coins = player["coins"]

def view_items():
    print("-------------------------------")
    print("Item         Price   Stock")
    print("-------------------------------")
    for item, details in store.items():
        print(f"{item:<13} {details['price']:<8} {details['stock']:}")
    print()    
    return

def get_coins():
    print(f"💰 You Have {player["coins"]} coins")
    return player["coins"]

def add_coins(coins):
    try:
        amount = int(input("enter how much coins you got to add: \n"))
        player["coins"] += amount
        with open("player.json", "w") as f:
            json.dump(player, f, indent=4)
        return coins 
    except ValueError:
        print("Enter A Valid Number")

def buy_items():
    try:

        cart = input("enter the name of the items you want to buy: \n").strip().lower()
        amount = int(input("enter how many piece you wish to buy: \n"))

        for item, details in store.items():
            if item == cart:
                total_price = store[cart]["price"] * amount
                if details["stock"] >= amount:
                    if player["coins"] >= total_price:
                        player["coins"] -= total_price

                        found = False
                        for inv_item in player["inventory"]:
                            if cart in inv_item:
                                inv_item[cart] += amount
                                found = True
                                break
                        if not found:
                            player["inventory"].append({cart: amount})

                        print(f"Nice! You just bought {amount} {cart}(s)! 🛒")
                        print(f"Pleasure doing business! You’ve got {player['coins']} coins left in your pouch. 💼")

                        with open(player_path, "w") as f:
                            json.dump(player, f, indent=4)
                        break
                    else:
                        print("you dont have enought Money")
                        print(f"You need {total_price} and you only got {player["coins"]}")
                        break
                else:
                    print("the amount you want exceeds avalaible stock!")
                    print(f"In Stock {details["stock"]}")
                    break
        else:
            print("Invalid item!")
    except ValueError:
        print("Invalid Input. please enter a valid number for the amount")
       

def view_bag():
    print("\n🎒 Your Inventory")
    print("-" * 30)

    if not player["inventory"]:
        print("🕳️  Your bag is empty.")
    else:
        for item in player["inventory"]:
            for name,amount in item.items():
                print(f"{name.capitalize()} * {amount}")
    print("-" * 30)
    return player

def main_menu():
    while True:
        print("1 - View Shop Items")
        print("2 - View Coins")
        print("3 - Add Money")
        print("4 - Buy Items")
        print("5 - View Your bag")
        print("6 - Save & EXIT")
        try:
            choice = int(input("enter the options you want to use: \n"))
            if choice == 1 :
                view_items()
                print()
            elif choice == 2:
                get_coins()
                print()
            elif choice == 3:
                add_coins(coins)
                print()
            elif choice == 4:
                buy_items() 
                print()
            elif choice == 5:
                view_bag()
                print()
            elif choice == 6:
                print("GoodBye, Have a great Day")
                with open(player_path, "w") as f:
                    json.dump(player, f, indent=4)
                return False
        except ValueError:
            print("please enter A Valid Number")


main_menu()
