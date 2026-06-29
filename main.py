from fastapi import FastAPI

app = FastAPI()

#Home Route
@app.get("/")

def home():
    return{"message":"Home world from FastAPI VENV"}

#About Route
@app.get("/about")
def about():
    return{"message":"This is about page"}

#Users page
@app.get("/users")
def users():
    return{
        "users":["Harshada","Sandesh","Rohit"]
    }

#Dynamic Route(Path Parameter)
@app.get("/dynamic/{user_id}")
def get_user(user_id):
    return{"user_id": user_id}

#Dynamic Routes using datatype
@app.get("/dynamicNew/{user_id}")
def get_data(user_id: int):
    return{"user_id": user_id}

#Dynamic Routes(Query Parameter)
@app.get("/dynamicQuery")
def get_query(name):
    return{"Name": name}

#Dynamic Routes(Query Parameter)
#@app.get("/dynamicQuery")
#def get_query(name: str = None)://Optional parameters
#    return{"Name": name}

#Dynamic Routes(Default Parameter)
@app.get("/product")
def get_query(limit: int = 10):
    return{"limit": limit}

#Dynamic Routes(Multiple Parameter)
@app.get("/items")
def get_item(name: str = None, price: int = 0):
    return{
        "Name": name,
        "Price": price
        }
