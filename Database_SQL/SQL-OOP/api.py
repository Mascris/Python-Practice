from fastapi import FastAPI
from pydantic import BaseModel
from logic import UserManager, MovieManager, RentalSystem

app = FastAPI()

user_manager = UserManager()
movie_manager = MovieManager()
rental_system = RentalSystem()

class UserForm(BaseModel):
    name: str
    email: str
    password: str

class MovieForm(BaseModel):
    title: str
    genre: str
    daily_price: float
    stock: int

class RentalForm(BaseModel):
    user_email: str
    movie_title: str

class LoginForm(BaseModel):
    email: str
    password: str

@app.get("/")
def home():
    return {"message": "CineVault Beta API"}

@app.post("/users/add")
def add_users(form: UserForm):
    result = user_manager.add_user(form.name, form.email, form.password)
    return result

@app.get("login")
def user_login(form: LoginForm):
    return user_manager.login_user(form.email, form.password)

@app.post("/movies/add")
def add_movies(form: MovieForm):
    result = movie_manager.add_movie(form.title, form.genre, form.daily_price, form.stock)
    return result

@app.get("/movies/list")
def list_movies():
    movies = movie_manager.list_all_movies()
    return movies

@app.post("/rent")
def rent_movie(form: RentalForm):
    result = rental_system.rent_movie(form.user_email, form.movie_title)
    return result

@app.post("/return")
def return_movie(form: RentalForm):
    result = rental_system.return_movie(form.user_email, form.movie_title)
    return result

@app.get("/history/{email}")
def view_history(email: str):
    history = rental_system.view_user_history(email)
    return history
