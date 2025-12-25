from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, field_validator
from logic import UserManager, MovieManager, RentalSystem
from errors import UserNotFoundError, MovieNotFoundError, MovieOutOfStockError

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

    @field_validator('daily_price')
    @classmethod
    def check_price(cls, v: float) -> float:
        if v <= 0:
            raise ValueError('Price must be Positive')
        return v
    
    @field_validator('stock')
    @classmethod
    def check_stock(cls, v: int) -> int:
        if v < 0:
            raise ValueError('Stock cannont be Negative')
        return v
    

class RentalForm(BaseModel):
    user_email: str
    movie_title: str

class LoginForm(BaseModel):
    email: str
    password: str

@app.exception_handler(UserNotFoundError)
async def user_not_found_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc), "error_code": "User_Not_Found"}
    )

@app.exception_handler(MovieNotFoundError)
async def movie_not_found_handler(request: Request, exc: MovieNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc), "error_code": "Movie_Not_Found"}
    )

@app.exception_handler(MovieOutOfStockError)
async def movie_out_of_stock_handler(request: Request, exc: MovieOutOfStockError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc), "error_code": "Movie_Out_Of_Stock"}
    )

@app.get("/")
def home():
    return {"message": "CineVault Beta API"}

@app.post("/users/add")
def add_users(form: UserForm):
    result = user_manager.add_user(form.name, form.email, form.password)
    return result

@app.post("/login")
def user_login(form: LoginForm):
    return user_manager.login_user(form.email, form.password)

@app.post("/movies/add")
def add_movies(form: MovieForm):
    result = movie_manager.add_movie(form.title, form.genre, form.daily_price, form.stock)
    return result

@app.get("/movies/list")
def list_movies(page: int = 1, limit: int = 10):
    movies = movie_manager.list_all_movies(page=page, limit=limit)
    return movies

@app.post("/rent")
def rent_movie(form: RentalForm):
    result = rental_system.rent_movie(form.user_email, form.movie_title)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result

@app.post("/return")
def return_movie(form: RentalForm):
    result = rental_system.return_movie(form.user_email, form.movie_title)
    return result

@app.get("/history/{email}")
def view_history(email: str):
    history = rental_system.view_user_history(email)
    return history
