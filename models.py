from sqlalchemy import Column, Integer, String
from database import Base


# Table within the database we are creating
class Books(Base):
    __tablename__ = "books"  # SQLAlchemy specific table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)
