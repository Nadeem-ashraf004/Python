from fastapi import FastAPI, HTTPException
from typing import List, Optional    
from pydantic import BaseModel
app=FastAPI()
#database class
class database:
    def __init__(self):
        self.db=[]
    def add_blog_post(self,blog_post:dict):
        self.db.append(blog_post)
    def get_blog_post(self):
        return self.db        
db=database()
class Blogpost(BaseModel):
    title:str
    content:Optional[str]=None
@app.post("/create_blog_post")
async def create_blog_post(blog_post:Blogpost):
    if not blog_post.title:
        raise HTTPException(status_code=400, detail="title is requred")
    db.add_blog_post(blog_post.dict())
    return{"massage ":"blog created succesfuly"}
@app.get("/get_blog_posts", response_model=List[Blogpost])
async def get_blog_posts():
    # Returning the list of blog posts from the imaginary database
    return db.get_blog_posts()    
        