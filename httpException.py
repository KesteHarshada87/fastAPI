from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# HTTPException
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "id": 1,
        "name": "Harshada"
    }

# Custom Exception
class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

# Global Exception Handler
@app.exception_handler(UserNotFoundException)
async def user_not_found(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exc.name} not found"
        }
    )

# Route
@app.get("/users/{name}")
def get_user_by_name(name: str):
    if name != "Harshada":
        raise UserNotFoundException(name)

    return {
        "name": name
    }