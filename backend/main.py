from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    price: int
    tax: Optional[float] = None
    description: Optional[str] = None


class CreateItemDto(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/hello")
def read_hello():
    return {"message": "Hello World2"}


@app.post("/items/")
def create_item(item: CreateItemDto):
    return {
        "message": "Item created successfully",
        "data": {
            "name": item.shopInfo.name,
            "price": item.shopInfo.location,
            "items": item.items,
        },
    }
