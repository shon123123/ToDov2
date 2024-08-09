from sqlalchemy.orm import Session
from . import models, schemas

def get_todo_items(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of todo items from the database with pagination.

    Parameters:
    - db (Session): The database session.
    - skip (int): The number of records to skip (for pagination).
    - limit (int): The maximum number of records to return.

    Returns:
    - List[models.TodoItem]: A list of todo items.
    """
    return db.query(models.TodoItem).offset(skip).limit(limit).all()

def create_todo_item(db: Session, todo: schemas.TodoItemCreate):
    """
    Create a new todo item in the database.

    Parameters:
    - db (Session): The database session.
    - todo (schemas.TodoItemCreate): The todo item data to create.

    Returns:
    - models.TodoItem: The created todo item.
    """
    # Create a new TodoItem instance from the provided schema
    db_todo = models.TodoItem(**todo.dict())
    # Add the new todo item to the session
    db.add(db_todo)
    # Commit the transaction to save the new item to the database
    db.commit()
    # Refresh the instance to get updated data (like auto-generated fields)
    db.refresh(db_todo)
    return db_todo

def get_todo_item(db: Session, todo_id: int):
    """
    Retrieve a specific todo item by its ID.

    Parameters:
    - db (Session): The database session.
    - todo_id (int): The ID of the todo item to retrieve.

    Returns:
    - models.TodoItem: The retrieved todo item, or None if not found.
    """
    return db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()

def delete_todo_item(db: Session, todo_id: int):
    """
    Delete a specific todo item by its ID.

    Parameters:
    - db (Session): The database session.
    - todo_id (int): The ID of the todo item to delete.

    Returns:
    - None
    """
    # Delete the todo item with the given ID
    db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).delete()
    # Commit the transaction to apply the deletion
    db.commit()

def update_todo_item(db: Session, todo_id: int, todo: schemas.TodoItemCreate):
    """
    Update an existing todo item with new data.

    Parameters:
    - db (Session): The database session.
    - todo_id (int): The ID of the todo item to update.
    - todo (schemas.TodoItemCreate): The new data to update the todo item with.

    Returns:
    - None
    """
    # Update the todo item with the given ID using the new data
    db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).update(todo.dict())
    # Commit the transaction to apply the updates
    db.commit()
