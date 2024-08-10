- `main.py`: FastAPI application with CRUD endpoints.
- `crud.py`: Functions for interacting with the database.
- `models.py`: SQLAlchemy models.
- `schemas.py`: Pydantic schemas for data validation.
- `database.py`: Database connection and session management.

**----Necessary Installations for backend----**

    1. FastAPI - A modern, fast web framework for building APIs with Python.
    2. Uvicorn - A lightning-fast ASGI server for serving FastAPI applications.
        ( --<pip install uvicorn>--)
    2. SQLAlchemy - A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
        ( --<pip install sqlalchemy psycopg2>--)
    4. Psycopg2 - A PostgreSQL database adapter for Python.
    5. Pydantic - Data validation and settings management using Python type annotations.
    ----Commands to install----
        -> ( --<pip install uvicorn>--)
        -> ( --<pip install sqlalchemy psycopg2>--)
        -> ( --<pip install fastapi uvicorn psycopg2-binary>--)
  

## Setup

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
2.   **Activate the Virtual Environment:**
    venv\Scripts\activate

3. **Install Dependencies:**
    Install Dependencies:

4. **Run the Application:**
    uvicorn app.main:app --reload

**-------About--------**

    This backend is built using FastAPI and PostgreSQL to handle the CRUD operations for a Todo application. It includes essential endpoints for creating, reading, updating, and deleting todo items. The backend is designed with an optimized and modular code structure to ensure scalability and maintainability.



