from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/create")
def create_item(item: Item):
    total_cost = item.price * 1.20

    return{
        "item_name": item.name,
        "original_price": item.price,
        "price_with_tax": total_cost,
        "is_offer": item.is_offer
    }
