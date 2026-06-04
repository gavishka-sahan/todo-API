from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()

# In-memory store (no DB yet)
todos = {}

class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/todos")
def get_todos():
    return list(todos.values())

@app.get("/todos/{todo_id}")
def get_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

@app.post("/todos", status_code=201)
def create_todo(todo: Todo):
    todo_id = str(uuid.uuid4())
    todos[todo_id] = {"id": todo_id, **todo.dict()}
    return todos[todo_id]

@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, update: TodoUpdate):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    for field, value in update.dict(exclude_unset=True).items():
        todos[todo_id][field] = value
    return todos[todo_id]

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]