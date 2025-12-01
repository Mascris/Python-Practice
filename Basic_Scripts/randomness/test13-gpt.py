def get_balance():
    return 0

def Deposit(balance):
    try:
        deposit_amount = int(input("Enter the amount you want to Deposit: "))
        balance += deposit_amount
        print("Deposit successful. New balance:", balance)
    except ValueError:
        print("Please enter a valid number.")
    return balance

def check_balance(balance):
    print("Your balance is:", balance)
    return balance

def withdraw(balance):
    try:
        withdraw_amount = int(input("Enter the amount you want to Withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Withdrawal successful. New balance:", balance)
        else:
            print("Insufficient funds. Your balance is:", balance)
    except ValueError:
        print("Please enter a valid number.")
    return balance

def get_menu():
    balance = get_balance()
    while True:
        print("\nMenu:")
        print("1 = Check Balance")
        print("2 = Deposit")
        print("3 = Withdraw")
        print("4 = Exit")
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                check_balance(balance)
            elif choice == 2:
                balance = Deposit(balance)
            elif choice == 3:
                balance = withdraw(balance)
            elif choice == 4:
                print("Thank you for using the bank simulator. Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    get_menu()

main()

