inventory = {
    "apple" : {"stock": 15, "price": 6},
    "banana" : {"stock": 12, "price": 3},
    "beef" : {"stock": 25, "price": 22},
    "chicken" : {"stock": 20, "price": 17},
    "tomato" : {"stock": 30, "price": 5},
    "potato" : {"stock": 27, "price": 7},
    "onions" : {"stock": 55, "price": 2}
    }
def get_balance():
    balance = 0
    return balance

def all_items():
    print("-----------------------")
    print("Item     Price   Stock")
    print("-----------------------")
    for item, details in inventory.items():
        print(f"{item:<8} {details['price']:<7} {details['stock']}")
    return

def buy_item(balance,inventory):
    cart = input("enter the item you want to purchase: \n")
    amounts = int(input("enter how many of this item you want: \n"))
    for item, details in inventory.items():
        if item == cart:
            if details["stock"] >= amounts:
                if details["price"] <= balance:
                    print("Your items have been successfully purchased")
                    print(f"you have buyed {amounts} {cart} successfully!")       
                else:
                    print("you dont have enough money to make this purchase")
                    break
            else:
                print("the amount you want is not possible")
        else:
            print("this item is not listed in out shop")
    return


def add_money(balance):
    try:
        amount = int(input("Enter The Amount You Want To ADD: "))
        balance += amount
        print("Success your money has been added!")
    except ValueError:
        print("Please enter a valid Number")
    return balance


def check_balance(balance):
    print(f"your balance is: {balance}$")
    return balance

def main_menu():
    balance = get_balance()
    while True:
        print("1 = Check All items ")
        print("2 = Check Balance ")
        print("3 = Add Balance")
        print("4 = buy Items")
        print("5 = EXIT")
        try:
            choice = int(input("Select options:  "))
            if choice == 1:
                all_items()
            elif choice == 2:
                balance = check_balance(balance)
                print("-----------------------")
            elif choice == 3:
                balance = add_money(balance)
                print("-----------------------")
            elif choice == 4:
                balance = buy_item(balance,inventory)  
                print("-----------------------")
            elif choice == 5:
                print("GoodBye, thank you for your service")
                return False
            else:
                print("Please Select a Valid Number between 1 -- 5 ")

        except ValueError:
            print("Please enter a Number")
            print("-----------------------")

def main():
    main_menu()

main()


