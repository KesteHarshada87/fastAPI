from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

def verify_token(token: str = Header(None)):
    if token != "mysecreteToken":
        raise HTTPException(
            status_code = 401,
            details = "unauthorized user"
        )
    return{
        "user": "Authorized user"
    }

@app.get("/secure_data")
def secure_data(user = Depends(verify_token)):
    return{
        "message": "secure data accessed",
        "user": user
    }
