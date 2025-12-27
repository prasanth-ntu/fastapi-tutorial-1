# Fastapi Tutorial

## YouTube: [Python FastAPI Tutorial: How to build modern RESTful APIs with Python](https://www.youtube.com/watch?v=MCVcAAoDJS8&list=PLK8U0kF0E_D6l19LhOGWhVZ3sQ6ujJKq_&index=2)

### Step 1: Install poetry
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
Visit this URL in the browser to see the result from the server (for the GET request)
```json
{
  "Welcome to the API to manage books": "Santh"
}
```

Visit http://127.0.0.1:8000/docs to see the auto-generated Swagger UI documentation embedded within the application.
![FastAPI doc auto-generated](static/fast-api-doc-1.png)


**Dummy content for testing**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Eric's Fast API Course",
  "author": "Eric Roby",
  "description": "The quickest way to learn FastAPI",
  "rating": 100
}

{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Example Title",
  "author": "Example Author",
  "description": "Example Description",
  "rating": 90
}
```