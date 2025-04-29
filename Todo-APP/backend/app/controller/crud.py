from app.models.model import TodoCreate,TodoOutput
from typing import List,Optional
from app.database import db_model
from app.database.db import engine, SessionLocal
from sqlalchemy.orm import Session

db_model.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_todos(db: Session) -> List[db_model.Todos]:
    return db.query(db_model.Todos).all()

def create_todo(todo: TodoCreate, db: Session) -> db_model.Todos:
    todo_model = db_model.Todos(title=todo.title, description=todo.description)
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

def get_todo_by_id(todo_id: int,db:Session) -> TodoCreate:
    return db.query(db_model.Todos).filter(db_model.Todos.id == todo_id).first()

def update_todo(todo_id: int, todo: TodoCreate, db: Session) -> TodoCreate:
    db_todo = db.query(db_model.Todos).filter(db_model.Todos.id == todo_id).first()
    if not db_todo:
        return None
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(todo_id: int, db: Session) -> TodoCreate:
    db_todo = db.query(db_model.Todos).filter(db_model.Todos.id == todo_id).first()
    if not db_todo:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo