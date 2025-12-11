from db import connect
from models import User,Movie,Rental
import datetime
from tabulate import tabulate

class UserManager:
    def __init__(self) -> None:
        pass

    def add_user(self,name: str,email: str):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("insert into users(name,email)values(%s,%s)",(name,email))
                    conn.commit()
        except Exception as e:
            print(f"ERROR: adding User {e}.")

    def find_user_by_email(self,email):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT user_id, name, email from users where email = %s"
                    cursor.execute(sql, (email,))
                    row = cursor.fetchone()
                    if not row:
                        print("movie not found")
                        return None

                    if row:
                        return User(row[0], row[1],row[2])

        except Exception as e:
            print(f"ERROR: finding user: {e}.")
            return None

class MovieManager:
    def __init__(self) -> None:
        pass

    def add_movie(self,title: str,genre: str,daily_price: float,stock:int):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT title from movies where title = %s",(title,))
                    if cursor.fetchone():
                        print(f"this Movie title: {title} is already exist")
                        return None

                    sql = "insert into movies (title,genre,daily_price,stock) values (%s,%s,%s,%s)"
                    cursor.execute(sql,(title,genre,daily_price,stock))
                    row = cursor.fetchone()
                    conn.commit()
                    if row:
                        return Movie(0,row[1],row[2],row[3],row[4])

        except Exception as e:
            print(f"ERROR: adding movie {e}.")


    def list_all_movies(self):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT movie_id, title, genre, daily_price, stock from movies"
                    cursor.execute(sql,)
                    row = cursor.fetchall()

                    if row:
                        return User(row[0],row[1],row[2],row[3],row[4])
                    return None

        except Exception as e:
            print(f"ERROR: Listing movies {e}.")
     
    def list_movie_by_title(self,title):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT title,genre,daily_price,stock from movies where title = %s"
                    cursor.execute(sql,(title,))
                    row = cursor.fetchone()
                    
                    if not row:
                        print("email not found!")
                        return None

                    if row :
                        return Movie(row[0],row[1],row[2],row[3],row[4])
        except Exception as e:
            print(f"ERROR: Listing movies by this title {e}.")


class RentalSystem:
    def __init__(self) -> None:
        pass
    
    def rent_movie(self,user_email,movie_title):
        user_tool = UserManager()
        movie_tool = MovieManager()

        user = user_tool.find_user_by_email(user_email)
        movie = movie_tool.list_movie_by_title(movie_title)

        today = datetime.date.today()
        due_date = today + datetime.timedelta(days=7)


        if not user:
            print(f"this {user_email} doesnt exist.")
            return 
    
        if not movie:
            print(f"this {movie_title} not found.")
            return

        if movie.stock >= 1:
            print(f"{movie_title} is currently out of stock!")
            return

        try:
             with connect() as conn:
                 with conn.cursor() as cursor:
                    sql_rent = "INSERT INTO rentals (user_id,movie_id,rental_date,due_date,return_date) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql_rent, (user.user_id, movie.movie_id, today, due_date))
                    
                    sql_update = "UPDATE movies SET stock = stock -1 where movie_id = %s"
                    cursor.execute(sql_update, (movie.movie_id,))
                    
                    conn.commit()
                    print("you've been added successfuly")

        except Exception as e:
            print(f"ERROR: {e}")

    def return_movie(self,user_email,movie_title):

        user_tool = UserManager()
        movie_tool = MovieManager()
    
        user = user_tool.find_user_by_email(user_email)
        movie = movie_tool.list_movie_by_title(movie_title)

        today = datetime.date.today()

        if not user:
            print(f"this user: {user_email} doesnt exist!")
            return

        if not movie:
            print(f"this movie: {movie_title} is not found!")
            return

        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT rental_id FROM rentals where user_id = %s AND movie_id = %s AND return_date IS NULL"
                    cursor.execute(sql, (user.user_id, movie.movie_id))

                    row = cursor.fetchone()

                    if not row:
                        print(f"This user does not currently have this movie: '{movie_title}' rented.")
                        return
                    
                    rental = row[0]
                    print(f"the active rental ID: {rental}")

                    sql_update = "UPDATE rentals SET return_date = %s WHERE rental_id = %s"
                    cursor.execute(sql_update, (today, rental))

                    sql_add = "UPDATE movies SET stock = stock + 1 WHERE movie_id = %s"
                    cursor.execute(sql_add,(movie.movie_id))

                    conn.commit()

                    print(f"Success! '{movie_title}' has been returned on {today}.")
        except Exception as e:
            print(f"ERROR: {e}.")
    
    def view_user_history(self,user_email):
        try:
            print("f")

        except Exception as e:
            print(f"ERROR: {e}.")




