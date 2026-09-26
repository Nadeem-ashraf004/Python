from fastapi import FastAPI , HTTPException , Depends , Header
from jose import jwt ,JWTError
from datetime import datetime , timedelta ,timezone

app = FastAPI()

SECRET_KEY = "make first scret key using jwt"

ALGORITHM = "HS256"
#create the jwt token its a basic token generation process
def create_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp" : expire
    })
    token = jwt.encode(to_encode , SECRET_KEY ,algorithm= ALGORITHM)

    return token
# generate token base on login api

@app.post("/login")
def login(username : str , password: str):
    if username != "adem" or password !="12345":
        raise HTTPException (
            status_code = 401,
            datail ="user and password invalid ",
        )
    token = create_token({
        "sub":username
    })
    return {
        "access_token " : token,
        "token_type" : "bearer"
    }
#token varify 
def varify_token(token :str = Header(None)):
    try :
        paylaod =jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)
        return paylaod
    except:
        raise HTTPException(
            status_code = 401,
            detail = "invalid or expire token"
        )
    #protected ruote
@app.get("/secure")
def sure_data(user =Depends(varify_token)):
    return{
        "message " : "secure data access",
        "user" : user
    }
