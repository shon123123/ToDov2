from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL for the PostgreSQL database
# Format: postgresql://user:password@host:port/database
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:shon2013@localhost:5432/todo'

# Create the SQLAlchemy engine
# This engine will be used to connect to the PostgreSQL database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
# The sessionmaker function returns a new session class bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models
# This base class will be inherited by all our models
Base = declarative_base()
