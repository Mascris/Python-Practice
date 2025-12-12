from logic import UserManager, MovieManager, RentalSystem

def main_menu(rental,movie,user):
    while True:
        print("\n=== SQL Inventory Manager ===")
        print("1 - Add a new User")
        print("2 - Add a new Movie")
        print("3 - Rent a movie")
        print("4 - Return a movie")
        print("5 - View History")
        print("6 - List all Movies") 
        print("7 - Exit")

        try:
            choice = input("\nChoose an Option: ")

            if choice == "1":
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                user.add_user(name, email)

            elif choice == "2":
                title = input("Enter Title: ")
                genre = input("Enter Genre: ")
                daily_price = float(input("Enter Price: "))
                stock = int(input("Enter stock: "))
                movie.add_movie(title, genre, daily_price, stock)

            elif choice == "3":
                user_email = input("Enter User Email: ")
                movie_title = input("Enter Movie Title: ")
                rental.rent_movie(user_email,movie_title)

            elif choice == "4":
                user_email = input("Enter User Email: ")
                movie_title = input("Enter Movie Title: ")
                rental.return_movie(user_email,movie_title)

            elif choice == "5":
                user_email = input("Enter Email: ")
                rental.view_user_history(user_email)

            elif choice == "6":
                movie.list_all_movies()

            elif choice == "7":
                print("GoodBye!")
                break

            else:
                print("Enter a Valid Option!")


        except Exception as e:
            print(f"ERROR: {e}.")


if __name__ == "__main__":

    rental_system = RentalSystem()
    movie_manager = MovieManager()
    user_manager = UserManager()

    main_menu(rental_system, movie_manager, user_manager)
