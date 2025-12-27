# Will create RESTful API for books here

from typing import Counter
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field # For data validation and parsing
from uuid import UUID

app = FastAPI() # FastAPI instance

# Pydantic model for the Book resource
class Book(BaseModel): 
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=1000)
    rating: int = Field(gt=-1, lt=101) # Rating should be between 0 and 100

BOOKS = [] # This is a list of books

# @app.get("/{name}") # This is a path parameter for the GET request
# def read_api(name: str):
#     return {"Welcome to the API to manage books": name}

@app.get("/") # This is a root path for the GET request
def get_all_books() -> list[Book]:
    return BOOKS

@app.post("/") # This is a root path for the POST request
def create_book(book: Book) -> Book:
    BOOKS.append(book) 
    return book 

### For loop based implementation ###
"""
@app.put("/{book_id}") # This is a path parameter for the PUT request
def update_book(book_id: UUID, book: Book) -> Book:
    counter = 0

    for x in BOOKS:
        if x.id == book_id:
            BOOKS[counter] = book
            return BOOKS[counter]
        counter += 1

    raise HTTPException(
        status_code=404, 
        detail="Book with id {book.id} not found"
    )

@app.delete("/{book_id}") # This is a path parameter for the DELETE request
def delete_book(book_id: UUID) -> str:
    counter = 0
    
    for x in BOOKS:
        if x.id == book_id:
            BOOKS.pop(counter)
            return f"Book with id {book_id} deleted"
        counter += 1

    raise HTTPException(
        status_code=404, 
        detail="Book with id {book_id} not found"
    )
"""

### Iterator based implementation ###
@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book) -> Book:
    # Find the index of the item to update
    item_index = next((index for (index, d) in enumerate(BOOKS) if d.id == book_id), None)
    
    # Check if book exists
    if item_index is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Book with id {book_id} not found"
        )
    
    BOOKS[item_index] = book
    return book

@app.delete("/{book_id}")
def delete_book(book_id: UUID) -> str:
    # Find the index of the item to delete
    item_index = next((index for (index, d) in enumerate(BOOKS) if d.id == book_id), None)
    
    # Check if book exists
    if item_index is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Book with id {book_id} not found"
        )
    
    BOOKS.pop(item_index)
    return f"Book with id {book_id} deleted"