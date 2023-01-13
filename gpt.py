from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

itemm = []

class Item(BaseModel):
    """defines a schema for an item"""
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/itemm/")
async def create_item(item: Item):
    itemm.append(item)
    return {"item": item.dict()}

@app.get("/itemm/")
async def read_itemm():
    return {"itemm": [item.dict() for item in itemm]}
