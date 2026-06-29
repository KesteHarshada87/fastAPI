from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

#post
@app.post("/todos")    
def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message": "todo created",
        "data": todo
    }

#read all data
@app.get("/todos")
def get_todos():
    return todos

#read single data using path parameters
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo.id:
            return todo
    return{
        "error": "Todo not found"
    }  

#update api
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, update_todo:Todo):
   for index,todo in enumerate(todos):
       if todo.id == todo.id:
           todos[index] = update_todo
       return{
           "message": "Data updated",
           "data": update_todo

       }
   return{
       "error": "Todo not found"
   }

#delete api
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo.id:
            todos.pop(index)
        return{
            "message": "Data deleted",
        }
    return{
        "error": "Todo not found"
    }    