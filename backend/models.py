from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class TodoItem(Base):
    """
    SQLAlchemy model for the 'todo_items' table.
    
    Attributes:
    - id (int): Primary key, auto-incremented integer.
    - title (str): Title of the todo item.
    - description (str): Description of the todo item.
    - completed (bool): Status indicating whether the todo item is completed.
    """
    __tablename__ = "todo_items"

    # Primary key for the table
    id = Column(Integer, primary_key=True, index=True)
    # Title of the todo item with an index for faster queries
    title = Column(String, index=True)
    # Description of the todo item with an index for faster queries
    description = Column(String, index=True)
    # Boolean flag to indicate if the todo item is completed or not
    completed = Column(Boolean, default=False)
