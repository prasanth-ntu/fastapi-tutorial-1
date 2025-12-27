# [How to build a FastAPI app with PostgreSQL](https://www.youtube.com/watch?v=398DuQbQJq0&list=PLK8U0kF0E_D6l19LhOGWhVZ3sQ6ujJKq_&index=5)

> [!SUMMARY] FastAPI application (a quiz game) with all the CRUD operation that's connected to the DB

```bash
# Project structure
|- main.py            # Main FastAPI file
|- database.py
|- models.py
|- pyproject.toml
|- README.md
```

## Prerequisites
- **Python**: `>= 3.14` (see `pyproject.toml`)
- **Poetry**: for dependency management
- **PostgreSQL**: local instance (or remote)
- **pgAdmin** (optional): GUI for inspecting/setting up your DB

## Step 1: Install dependencies
```bash
poetry install
```

## Step 2: Install PostgreSQL
Find the latest version in [postgresql.org](https://www.postgresql.org/) and install (with [Homebrew](https://formulae.brew.sh/formula/postgresql@18) for Mac).
```bash
# In Mac
$ brew update
$ brew install postgresql@18
```

Add PostgreSQL to your PATH (required because it's keg-only)
```bash
# Find the details
$ brew info postgresql@18 
==> postgresql@18: stable 18.1 (bottled) [keg-only]
...
If you need to have postgresql@18 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"' >> /Users/user/.zshrc
...

# Add it to our path
$ echo 'export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"' >> ~/.zshrc

$ source ~/.zshrc  # or restart your terminal

# Verify psql is running
$ psql --version
psql (PostgreSQL) 18.1 (Homebrew)
```

## Step 3: Start the PostgreSQL service
```bash
$  brew services start postgresql@18

# Verify
$ brew services list | grep postgres 
postgresql@18 started         user ~/Library/LaunchAgents/homebrew.mxcl.postgresql@18.plist
```

## Step 4: (Optional) Install pgAdmin
Official download: [pgadmin.org](https://www.pgadmin.org/download/pgadmin-4-macos/)

## Step 5: Create the database + user
This project currently uses a hard-coded connection string in `database.py`:

```text
postgresql://user:postgres@localhost:5432/QuizApplicationYT
```

That means:
- **username**: `user`
- **password**: `postgres`
- **database**: `QuizApplicationYT`

Create them in Postgres (one-time):

```bash
psql -U postgres
```

```sql
CREATE USER "user" WITH PASSWORD 'postgres';
CREATE DATABASE "QuizApplicationYT" OWNER "user";
GRANT ALL PRIVILEGES ON DATABASE "QuizApplicationYT" TO "user";
```

If you prefer different credentials/db name, update `URL_DATABASE` in `database.py`.

## Step 6: Setup Quiz Server & DB (pgAdmin screenshots)
![Setup `Quiz` Server](static/quiz-server-setup.png)
![Setup `QuizApplicationYT` DB](static/quiz-tables-added.png)

## Step 7: Run the FastAPI server
```bash
$ uvicorn main:app --reload 
```

Visit the Swagger docs: `http://127.0.0.1:8000/docs`

## Sample request body
```json
{
  "question_text": "What's the best Python Framework for HTTP based API server?",
  "choices": [
    {
      "choice_text": "FastAPI",
      "is_correct": true
    },
   {
      "choice_text": "Anything else",
      "is_correct": false
    }
  ]
}
```

# Few notes

## Formatting and Linting
Inside the venv, run
```bash
$ ruff format .
$ ruff check .
```