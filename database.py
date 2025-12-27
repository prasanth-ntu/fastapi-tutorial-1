from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Path to our local instance/installation of PostgreSQL
URL_DATABASE = "postgresql://user:postgres@localhost:5432/QuizApplicationYT"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
