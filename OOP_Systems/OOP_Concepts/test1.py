class BankAccount:
    def __init__(self,name,pin,balance=0) -> None:
        self.name = name
        self.balance = balance
        self.pin = pin
        self.history = []
        
    def get_balance(self):
        print(f"your balance is: {self.balance}.")
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        print(f"your balance is: {self.balance} after the deposit.")
        self.history.append(f"Deposit {amount}. New balance: {self.balance}.")
        return self.balance
    
    def withdraw(self):
        pinentre = int(input("please enter the pin code: "))

        if pinentre == self.pin:
            money = int(input("enter the amount to Withdraw: "))
            if self.balance >= money:
                self.balance -= money
                print(f"your balance is: {self.balance} after the Withdraw.")
                self.history.append(f"successfully Withdraw {money}")

            else:
                print("Not enough money to Withdraw!")
                self.history.append("not enough money to Withdraw")

            return self.balance
        else:
            print("The PIN is incorrect!")
            self.history.append("you've entered wrong PIN!")
            return

    def show_owner(self):
        print(f"the Owner of Account is: {self.name}.")
        return
    
    def show_history(self):
        for item in self.history:
            print(item)



account = BankAccount("Lassa",3333)
account2 = BankAccount("Mopo",6666)

account.deposit(500)
account.withdraw()
account.get_balance()
account.show_history()

