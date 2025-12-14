from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello,{name}."}

@app.get("/square/{number}")
def square(number: int):
    result = number * number
    return {f"the square of {number} is {result}."}
