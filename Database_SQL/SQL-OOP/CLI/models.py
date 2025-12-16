class User:
    def __init__(self,user_id: int,name: str,email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"Name: {self.name}, email: {self.email}"

class Movie:
    def __init__(self,movie_id: int,title: str,genre: str,daily_price: float,stock: int):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.daily_price = daily_price
        self.stock = stock

class Rental:
    def __init__(self,rental_id,user_id,movie_id,rental_date,due_date,return_date):
        self.rental_id = rental_id
        self.user_id = user_id
        self.movie_id = movie_id
        self.rental_date = rental_date
        self.due_date = due_date
        self.return_date = return_date
