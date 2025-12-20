from errors import UserNotFoundError, MovieOutOfStockError, MovieNotFoundError
from auth import TokenManager
import bcrypt
from db import connect
from models import User, Movie, Rental
import datetime

class UserManager:
    def __init__(self) -> None:

        pass

    def add_user(self, name: str, email: str, password: str):
        try:
            password_bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_bytes = bcrypt.hashpw(password_bytes, salt)
            hashed_string = hashed_bytes.decode('utf-8')

            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "insert into users(name, email, password_hash)values(%s, %s, %s)"
                    cursor.execute(sql, (name, email, hashed_string))
                    conn.commit()
                    return {"message": f"User '{name}' added successfully", "status": "success"}

        except Exception as e:
            return {"error": str(e), "status": "error"}

    def find_user_by_email(self, email):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT user_id, name, email from users where email = %s"
                    cursor.execute(sql, (email,))
                    row = cursor.fetchone()

                    if not row:
                        return None

                    if row:
                        return User(row[0], row[1], row[2])

        except Exception as e:
            print(f"ERROR: finding user: {e}.")
            return None

    def login_user(self,email: str,password: str):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT user_id, name, password_hash FROM users where email = %s"
                    cursor.execute(sql, (email,))
                    row = cursor.fetchone()

                    if not row: 
                        return {"Error": "Invalid email or password"}
                    
                    db_id = row[0]
                    db_name = row[1]
                    db_hash_str = row[2]

                    input_bytes = password.encode('utf-8')
                    hash_bytes = db_hash_str.encode('utf-8')
                    
                    if bcrypt.checkpw(input_bytes, hash_bytes):

                        auth = TokenManager()

                        access_token = auth.create_token(db_id, email)

                        return {
                        "message": f"welcome back, {db_name}",
                        "access_token": access_token,
                        "token_type": "bearer",
                        "status": "success"
                    }

                    else:
                        return {"message": "Invalid email or password"}

        except Exception as e:
            return {"Error": str(e), "status":"error"}

class MovieManager:
    def __init__(self) -> None:
        pass

    def add_movie(self, title: str, genre: str, daily_price: float, stock: int):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT title from movies where title = %s", (title,))
                    if cursor.fetchone():
                        return {"error": f"Movie '{title}' already exists", "status": "error"}

                    sql = "insert into movies (title,genre,daily_price,stock) OUTPUT INSERTED.movie_id, INSERTED.title, INSERTED.genre, INSERTED.daily_price, INSERTED.stock VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (title, genre, daily_price, stock))
                    row = cursor.fetchone()
                    conn.commit()

                    if row:
                        return {"message": f"Movie '{title}' added.", "status": "success", "id": row[0]}

        except Exception as e:
            print(f"ERROR: adding movie {e}.")
            return {"error": str(e), "status": "error"}

    def list_all_movies(self):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT title, genre, daily_price, stock from movies"
                    cursor.execute(sql)
                    rows = cursor.fetchall()

                    results = []
                    for row in rows:
                        movie_dict = {
                            "title": row[0],
                            "genre": row[1],
                            "daily_price": float(row[2]),
                            "stock": row[3]
                        }
                        results.append(movie_dict)

                    return results

        except Exception as e:
            print(f"Error: {e}")
            return []

    def list_movie_by_title(self, title):
        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT movie_id,title,genre,daily_price,stock from movies where title = %s"
                    cursor.execute(sql, (title,))
                    row = cursor.fetchone()
                    
                    if not row:
                        return None

                    if row:
                        return Movie(row[0], row[1], row[2], row[3], row[4])

        except Exception as e:
            print(f"ERROR: Listing movies by this title {e}.")
            return None

class RentalSystem:
    def __init__(self) -> None:
        pass
    
    def rent_movie(self, user_email, movie_title):
        user_tool = UserManager()
        movie_tool = MovieManager()

        user = user_tool.find_user_by_email(user_email)
        movie = movie_tool.list_movie_by_title(movie_title)

        today = datetime.date.today()
        due_date = today + datetime.timedelta(days=7)

        if not user:
            raise UserNotFoundError(f"User {user_email} doesn't exist")

        if not movie:
            raise MovieNotFoundError(f"Movie '{movie_title}' not Found")

        if movie.stock <= 0:
            raise MovieOutOfStockError(f"'{movie_title}' is out of stock")

        with connect() as conn:
            with conn.cursor() as cursor:
                sql_rent = "INSERT INTO rentals (user_id,movie_id,rental_date,due_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_rent, (user.user_id, movie.movie_id, today, due_date))
                
                sql_update = "UPDATE movies SET stock = stock - 1 where movie_id = %s"
                cursor.execute(sql_update, (movie.movie_id,))
                
                conn.commit()
                
                return {"message": f"Successfully rented '{movie_title}'!"}

    def return_movie(self, user_email, movie_title):
        user_tool = UserManager()
        movie_tool = MovieManager()
    
        user = user_tool.find_user_by_email(user_email)
        movie = movie_tool.list_movie_by_title(movie_title)

        today = datetime.date.today()

        if not user:
            return {"error": "User not found", "status": "error"}

        if not movie:
            return {"error": "Movie not found", "status": "error"}

        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT rental_id FROM rentals where user_id = %s AND movie_id = %s AND return_date IS NULL"
                    cursor.execute(sql, (user.user_id, movie.movie_id))

                    row = cursor.fetchone()

                    if not row:
                        return {"error": "Active rental not found for this user/movie.", "status": "error"}
                    
                    rental = row[0]

                    sql_update = "UPDATE rentals SET return_date = %s WHERE rental_id = %s"
                    cursor.execute(sql_update, (today, rental))

                    sql_add = "UPDATE movies SET stock = stock + 1 WHERE movie_id = %s"
                    cursor.execute(sql_add, (movie.movie_id,))

                    conn.commit()
                    return {"message": f"Success! '{movie_title}' returned.", "status": "success"}

        except Exception as e:
            return {"error": str(e), "status": "error"}
    
    def view_user_history(self, user_email):
        user_tool = UserManager()
        user = user_tool.find_user_by_email(user_email)

        if not user:
            return {"error": "User Not Found"}

        try:
            with connect() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT m.title, r.rental_date, r.due_date, r.return_date FROM movies m INNER JOIN rentals r ON m.movie_id = r.movie_id  WHERE r.user_id = %s"
                    cursor.execute(sql, (user.user_id,))
                    rows = cursor.fetchall()

                    history_list = []
                    for row in rows:
                        record = {
                            "movie_title": row[0],
                            "rental_date": row[1],
                            "due_date": row[2],
                            "return_date": row[3]
                        }
                        history_list.append(record)
                    
                    return history_list

        except Exception as e:
            print(f"ERROR: {e}")
            return []
