class Product:
    def __init__(self,name: str,product_id: str,price: float,stock_quantity: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock_quantity = stock_quantity

    def add_stock(self,amount: int):
        if amount <=0:
            print("the amount must be positive")
            return
        self.stock_quantity += amount

    def remove_stock(self,amount):
        if amount <=0:
            print("the amount must be positive")
            return
        self.stock_quantity -= amount

    def display_product_info(self):
        print(f"id:{self.product_id}, name:{self.name}, price:{self.price}, stock quantity:{self.stock_quantity}.")

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self,name,product_id,price,stock_quantity):
        if product_id in self.products:
            print(f"this {product_id} is already!")
            return
        new_product = Product(name,product_id,price,stock_quantity)
        self.products[product_id] = new_product

    def find_product(self,product_id):
        return self.products.get(product_id,None)

    def update_stock(self,product_id,amount_change):
        product = self.products.get(product_id)
        
        if not product:
            print("product not found")
            return
        if amount_change > 0:
            product.add_stock(amount_change)
            print(f"added {amount_change} units to {product.name}. new stock is {product.stock_quantity}.")

        elif amount_change < 0:
            amount_to_remove = abs(amount_change)

            if amount_to_remove > product.stock_quantity:
                print("not enough stock to widthdraw.")
                return

            product.remove_stock(amount_to_remove)
            print("removed successfully.")
            
        else:
            print("nothing to update amount to change cannot be 0.")
    def list_all_products(self):
        if not self.products:
            print("the store is empty!")
            return
        for product in self.products.values():
            product.display_product_info()

    def get_total_inventory_value(self):
        if not self.products:
            print("inventory is empty.")
            return 0

        total_price = 0
        total_stock = 0
        total = 0

        for _, data in self.products.items():
            total_price += data["price"]
            total_stock += data["stock_quantity"]
            total = total_stock * total_price
        print(f"the total of your inventory is {total_price} * {total_stock} = {total}!")
    
def main_menu(inventory):
    while True:
        print("\n=== GradeBook Menu ===")
        print("1 - Add a new product")
        print("2 - Update stock")
        print("3 - View products")
        print("4 - get Inventory value")
        print("5 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("enter products name: ")
            product_id = input("enter a product id: ")
            price = float(input("enter products price: "))
            stock_quantity = int(input("enter how many pieces you want to add: "))
            inventory.add_product(name,product_id,price,stock_quantity)
            print("your item have been added successfully!")

        elif choice == "2":
            print("still working on it!!")

        elif choice == "3":
            inventory.list_all_products()

        elif choice == "4":
            inventory.list_all_products()

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    inventory = InventoryManager()
    main_menu(inventory)
