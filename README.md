# [Python FastAPI Tutorial: How to Connect FastAPI to Database](https://www.youtube.com/watch?v=34jQRPssM5Q&list=PLK8U0kF0E_D6l19LhOGWhVZ3sQ6ujJKq_&index=3)

> [!SUMMARY] FastAPI application with all the CRUD operation that's connected to the DB

## Step 1: Install poetry
```bash
$ poetry install
```

## Step 2: Run our FastAPI app with auto-reload enabled for development.
```bash
uvicorn books:app --reload
INFO:     Will watch for changes in these directories: ['/Users/user/Projects/misc/fastapi-tutorial-1']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14165] using StatReload
INFO:     Started server process [14197]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 3: Visit the URL in browser

Our uvicorn is running in http://127.0.0.1:8000. 

Visit http://127.0.0.1:8000/docs to see the auto-generated Swagger UI documentation embedded within the application.

**Dummy content for testing**
```json
{
  "title": "Eric's Fast API Course",
  "author": "Eric Roby",
  "description": "The quickest way to learn FastAPI",
  "rating": 100
}

{
  "title": "Example Title",
  "author": "Example Author",
  "description": "Example Description",
  "rating": 90
}
```

# Few notes

## SQLAlchemy tracks objects differently for `CREATE` vs `UPDATE`

```
# CREATE - object starts "untracked"
book_model = models.Books(...)      # ❌ Not in session
db.add(book_model)                  # ✅ Now tracked
db.commit()                         # INSERT

# UPDATE - object starts "tracked"
book_model = db.query(...).first()  # ✅ Already tracked
book_model.title = "New"            # ✅ Change detected
# No db.add() needed!
db.commit()                         # UPDATE
```

## How Pydantic handles extra fields?

By default, Pydantic models ignore fields that aren't defined. So if someone sends:
```json
{
  "id": 999,
  "title": "New Book",
  "author": "Author Name",
  "description": "Book description",
  "rating": 85
}
```
The `id: 999` will be ignored because it's not in your `Book` model (in `books.py`). Pydantic will only parse:
- `title`
- `author`
- `description`
- `rating`

**This is a security feature**
This prevents users from trying to change the ID via the request body. The ID comes from the path parameter (`book_id`), not the body, which is the correct REST pattern.

## Formatting and Linting
Inside the venv, run
```bash
$ ruff format .
$ ruff check .
```