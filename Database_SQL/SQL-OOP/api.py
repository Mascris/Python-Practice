from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello! I am running on your PC!"}


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": a+b}
