from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from backend import crud, models, schemas
from .database import SessionLocal, engine 

from pydantic import BaseModel

class MyModel(BaseModel):
    class Config:
        from_attributes = True

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI()

# List of allowed origins for CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
      "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new todo item
@app.post("/todos/", response_model=schemas.TodoItem)
def create_todo_item(todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    return crud.create_todo_item(db=db, todo=todo)

# Endpoint to read all todo items with pagination
@app.get("/todos/", response_model=List[schemas.TodoItem])
def read_todo_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_todo_items(db, skip=skip, limit=limit)

# Endpoint to read a single todo item by ID
@app.get("/todos/{todo_id}", response_model=schemas.TodoItem)
def read_todo_item(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_item(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Endpoint to delete a todo item by ID
@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    crud.delete_todo_item(db, todo_id=todo_id)
    return {"ok": True}  

# Endpoint to update a todo item by ID
@app.put("/todos/{todo_id}", response_model=schemas.TodoItem)
def update_todo_item(todo_id: int, todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    crud.update_todo_item(db, todo_id=todo_id, todo=todo)
    return crud.get_todo_item(db, todo_id=todo_id)
