from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Settings and parameters for setting up the database instance
# ########################################################################################
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"  # This books.db is going to be created automatically by SQLAlchemy into our application

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite specific connection argument
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
