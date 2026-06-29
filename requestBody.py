from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#simple example
#@app.post("/create-user")
#def createUser(name: str, age: int):
#   return{
#      "name": name,
#     "age": age
#}

#for validation use pydantic
class User(BaseModel):
    name: str
    age: int


#Preferable
@app.post("/create-user")
def create_user(user:User):   
    return{
        "message": "User created",
        "data": user
    }

