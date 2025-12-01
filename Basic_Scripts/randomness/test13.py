def get_balance():
    balance = 0
    return balance

def deposit(balance):
    new_balance = int(input("enter the ampout you want to Deposit: ")) 
    new_balance = balance + new_balance
    print("the amount has been successfuly Deposit")
    return check_balance

def check_balance(new_balance):
    print("you Balance is: ", new_balance)
    return new_balance

def withdraw(balance):
    withdraw_amount = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW: "))
    if balance >= withdraw_amount:
        balance = balance - withdraw_amount
        print("Withdrawal successful. New balance:", balance)
    else:
        print("Insufficient funds.")
    return balance


def get_menu():
    amount1 = get_balance()
    print("1=check_balance / 2=Deposit / 3= withdraw / 4=exit")
    while True:
        menu = int(input("enter the action you want to procced: "))
        if menu == 1:
            check_balance(amount1)
        elif menu == 2:
            amount1 = deposit(amount1)
        elif menu == 3:
           amount1 =  withdraw(amount1)
        elif menu == 4:
            return False
        else:
            print("enter a number  between 1-4 '1=check_balance / 2=Deposit / 3= withdraw / 4=exit'")

def main():
    get_menu()

main()
