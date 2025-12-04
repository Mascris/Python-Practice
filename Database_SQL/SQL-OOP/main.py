from logic import UserManager, MovieManager, RentalSystem
def main_menu(rental,movie,user):
    try:
         while True:
             print("\n=== SQL Inventory Manager ===")
             print("1 - Add a new User")
             print("2 - Update stock")
             print("3 - Rent a movie")
             print("4 - return a movie")
             print("5 - History")
             print("6 - Exit")
        

            choice = input("choose an option: ")

    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    rental = RentalSystem()
    movie = MovieManager()
    user = UserManager()
    main_menu(rental,movie,user)
