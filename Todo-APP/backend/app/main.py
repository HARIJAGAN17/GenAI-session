from fastapi import FastAPI, HTTPException, Depends
from app.models.model import TodoCreate,TodoOutput
from app.controller.crud import get_todos, create_todo, get_todo_by_id, update_todo, delete_todo
from app.controller.crud import get_db
from sqlalchemy.orm import Session
from typing import List
from app.authentication.auth import get_current_user
from app.database import db_model
from fastapi.middleware.cors import CORSMiddleware
from app.authentication.auth_routes import router as auth_router
from app.gpt_model.gpt_route import router as gpt_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(gpt_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Todo app!"}

@app.get("/todos", response_model=List[TodoOutput])
def get_all_todos(db: Session = Depends(get_db)):
    return get_todos(db)

@app.post("/todos", response_model=TodoCreate)
def create_new_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: db_model.User = Depends(get_current_user)):

    return create_todo(todo, db)

@app.get("/todos/{todo_id}", response_model=TodoCreate)
def get_todo_by_id_route(todo_id: int,db: Session = Depends(get_db)):
    todo = get_todo_by_id(todo_id,db)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoCreate)
def update_todo_route(todo_id: int, todo: TodoCreate,db: Session = Depends(get_db)):
    updated_todo = update_todo(todo_id, todo,db)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@app.delete("/todos/{todo_id}", response_model=TodoCreate)
def delete_todo_route(todo_id: int,db: Session = Depends(get_db)):
    deleted_todo = delete_todo(todo_id,db)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted_todo
