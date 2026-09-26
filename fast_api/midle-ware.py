#corsmdelwarein fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
app=FastAPI()
#add fastapi midleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message":"CORS middleware is working!"}
#GzipMIddleware in fastapi
app.add_middleware(GZipMiddleware,minimum_size=1000)
@app.get("/large_response")
def large_response():
    large_data="A"*1000
    return {"data":large_data}
#trustedhost middleware
#app.add_middleware(TrustedHostMiddleware,allowed_hosts=["example.com","localhost","127.0.0.1:8000"])
#@app.get("/trusted_host")
#def trudted_host():
  #  return {"message":"trusted host middleware is working proparly with my own setuation"}
#HTTPredirect middleware
#app.add_middleware(HTTPSRedirectMiddleware,Redirect_url="http://127.0.0.1:8000")
#@app.get("/redirect")
#def redirect():
#    return{"message ":"redirect succesfullly"}
