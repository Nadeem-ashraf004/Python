from fastapi import Fastapi
from pydantic import basemodel
# creating app
app= FastApi()
#defining the item
class item(basemodel):
    name:str
    price:float
#defining api end point
#create
@app.post("/item/")
async def create_item(item:item):
    item_id=len(item)+1
    item[item_id]=item
    return{"id":item_id,"item":item}
#read
@app.get("/item/{item_id}")
async def read_item(item_id:int):
    return item.get(item_id,{"error":" item not found"})
#update
@app.update("/item/{item_id}")
async def update_item(item:item,item_id:int):
    if item[item_id] in teim:
        return {"message":"update item","item":item}
    return{"error":"item not found"}
#delete
@app.delete("/item/{item_id}")
async def delete_item(item_id:int):
    if item_id in item:
        delete_item=item.pop(item)
        return{"massage ":"item delete","item":delete_item}
    return{"error":"item not found"}
                

