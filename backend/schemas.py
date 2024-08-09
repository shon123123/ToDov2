from pydantic import BaseModel

class TodoItemBase(BaseModel):
    """
    Base schema for Todo items. Contains the common fields shared by 
    both the creation and read schemas.
    
    Attributes:
    - title (str): The title of the todo item.
    - description (str): The description of the todo item.
    """
    title: str
    description: str

class TodoItemCreate(TodoItemBase):
    """
    Schema for creating a new Todo item. Inherits from TodoItemBase 
    but does not add any additional fields. This is used when creating
    a new todo item.
    """
    pass

class TodoItem(TodoItemBase):
    """
    Schema for representing a Todo item that includes all fields,
    including those that are generated or managed by the database.
    
    Attributes:
    - id (int): The unique identifier for the todo item.
    - completed (bool): The completion status of the todo item.
    
    Config:
    - orm_mode: Set to True to enable compatibility with ORM models. 
      This allows Pydantic to work with SQLAlchemy models by using 
      the ORM object fields directly.
    """
    id: int
    completed: bool

    class Config:
        orm_mode = True
