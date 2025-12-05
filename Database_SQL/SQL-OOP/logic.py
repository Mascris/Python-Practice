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
                    sql = "SELECT name, email from users where email = %s"
                    cursor.execute(sql, (email,))
                    row = cursor.fetchone()
                    if not row:
                        print("movie not found")
                        return None

                    if row:
                        return User(row[0],row[1],row[2])

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
                    sql = "SELECT title,genre,daily_price,stock from movies"
                    cursor.execute(sql,)
                    row = cursor.fetchall()

                    if row:
                        return User(row[1],row[2],row[3],row[4])
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
                        return Movie(0,row[0],row[1],row[2],row[3])
        except Exception as e:
            print(f"ERROR: Listing movies by this title {e}.")


class RentalSystem:
    def __init__(self) -> None:
        pass
    
    def rent_movie(self,user_email,movie_title):
        user_email.find_user_by_email()
        movie_title.list_movie_by_title()

        today = datetime.date.today()
        due_date = today + datetime.timedelta(days=7)

        current_stock = row[4]
                            
