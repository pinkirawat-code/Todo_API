from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/todos", response_model=schemas.Todo)
def create(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)


@app.get("/todos", response_model=list[schemas.Todo])
def read_all(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_one(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo

@app.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.delete_todo(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Deleted successfully"}