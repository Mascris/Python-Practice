from db import connect  
class Product:
    def __init__(self, name: str, product_id: str, price: float, stock_quantity: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock_quantity = stock_quantity

    def display_product_info(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Price: {self.price} | Stock: {self.stock_quantity}")

class InventoryManager:
    def __init__(self):
        pass

    def add_product(self, name, product_id, price, stock_quantity):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT product_id FROM products WHERE product_id = %s", (product_id,))
                    if cursor.fetchone():
                        print(f"Error: Product ID {product_id} already exists!")
                        return

                    sql = "INSERT INTO products (name, product_id, price, stock_quantity) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (name, product_id, price, stock_quantity))
                    conn.commit()
                    print(f"Product '{name}' added to Database successfully!")
        except Exception as e:
            print(f"Error adding product: {e}")

    def find_product(self, product_id):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT name, product_id, price, stock_quantity FROM products WHERE product_id = %s"
                    cursor.execute(sql, (product_id,))
                    row = cursor.fetchone()
                    
                    if row:
                        return Product(row[0], row[1], row[2], row[3])
                    return None
        except Exception as e:
            print(f"Error finding product: {e}")
            return None

    def update_stock(self, product_id, amount_change):
        try:
            current_product = self.find_product(product_id)
            if not current_product:
                print("Product not found.")
                return

            new_quantity = current_product.stock_quantity + amount_change

            if new_quantity < 0:
                print("Error: Not enough stock to remove that amount.")
                return

            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE products SET stock_quantity = %s WHERE product_id = %s"
                    cursor.execute(sql, (new_quantity, product_id))
                    conn.commit()
            
            action = "Added" if amount_change > 0 else "Removed"
            print(f"Successfully {action} stock. New quantity: {new_quantity}")

        except Exception as e:
            print(f"Error updating stock: {e}")

    def list_all_products(self):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT name, product_id, price, stock_quantity FROM products")
                    rows = cursor.fetchall()
                    
                    if not rows:
                        print("The inventory is empty in the Database!")
                        return

                    print("\n--- Current Inventory (from SQL) ---")
                    for row in rows:
                        temp_product = Product(row[0], row[1], row[2], row[3])
                        temp_product.display_product_info()
        except Exception as e:
            print(f"Error listing products: {e}")

    def get_total_inventory_value(self):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT SUM(price * stock_quantity) FROM products"
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    
                    total_value = result[0] if result[0] else 0.0
                    print(f"Total value of inventory in Database: ${total_value:.2f}")
        except Exception as e:
            print(f"Error calculating total value: {e}")

def main_menu(inventory):
    while True:
        print("\n=== SQL Inventory Manager ===")
        print("1 - Add a new product")
        print("2 - Update stock")
        print("3 - View products")
        print("4 - Get Inventory value")
        print("5 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            pid = input("Enter product ID: ")
            price = float(input("Enter price: "))
            qty = int(input("Enter stock quantity: "))
            inventory.add_product(name, pid, price, qty)

        elif choice == "2":
            pid = input("Enter product ID: ")
            amount = int(input("Amount to add (positive) or remove (negative): "))
            inventory.update_stock(pid, amount)

        elif choice == "3":
            inventory.list_all_products()

        elif choice == "4":
            inventory.get_total_inventory_value()

        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    manager = InventoryManager()
    main_menu(manager)
