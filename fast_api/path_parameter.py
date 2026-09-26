from fastapi import FastAPI
import uvicorn 
from pydantic import BaseModel

app=FastAPI()

@app.get("/item/{item_id}")
async def read_item(item_id : int):
    return {"item_id" : item_id}
@app.post("/full_name")
async def create_name(full_name = str):
    return {"Full_Name " : full_name}
class Item(BaseModel):
    name:str
    description : str | None = None
    price :float
    tax : float | None =None
@app.get("/item")
async def read_Item(item:int):
    return {"item" : item}