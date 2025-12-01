from player import add_coins, get_inventory, get_players_data
from shop import get_store_items, buy_items

def menu():
    while True:
        print("\n--- Main Menu ---")
        print("1 - View Shop Items")
        print("2 - View Player Coins")
        print("3 - Add Coins to Player")
        print("4 - Buy Items")
        print("5 - View Your Inventory")
        print("6 - Save & EXIT")
        try:
            choice = int(input("enter the options you want to use: \n"))
            if choice == 1 :
                get_store_items()
                print()
            elif choice == 2:
                get_players_data()
                print()
            elif choice == 3:
                add_coins()
                print()
            elif choice == 4:
                buy_items()
                print()
            elif choice == 5:
                get_inventory()
                print()
            elif choice == 6:
                print("GoodBye, Have a great Day")
                return False
            else:
                print("please enter a Number between 1<-->6")
        except ValueError:
            print("please enter A Valid Number")


if __name__ == "__main__":
    menu()
