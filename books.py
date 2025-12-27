from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()  # FastAPI instance

# Create the database and the tables if they don't exist
models.Base.metadata.create_all(bind=engine)


# Dependency to get the database session to be used in the endpoints
def get_db():
    """
    Create a session to the database and yield it to the caller.
    The session will be closed after the caller is done with it.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic model for the Book resource
class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=1000)
    rating: int = Field(gt=-1, lt=101)  # Rating should be between 0 and 100


BOOKS = []


@app.get("/")
def get_all_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()  # Query the database for all the books


@app.post("/")
def create_book(book: Book, db: Session = Depends(get_db)) -> Book:
    book_model = models.Books(**book.model_dump())
    db.add(book_model)
    db.commit()

    return book


### Iterator based implementation ###
@app.put("/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)) -> Book:
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

    # Update the existing instance's attributes
    for key, value in book.model_dump().items():
        setattr(book_model, key, value)

    db.commit()
    # db.refresh(book_model)

    return book_model


@app.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)) -> str:
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

    db.delete(book_model)
    db.commit()
    return f"Book with id {book_id} deleted"
