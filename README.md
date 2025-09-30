# FastAPI + SQLAlchemy + Alembic Demo Project

This project demonstrates building a RESTful API using **FastAPI** with **PostgreSQL** as the database, managed via **SQLAlchemy ORM** and **Alembic** for database migrations. It is designed to teach CRUD operations, database versioning, and schema evolution.

---

## Features

- **User Management API**
  - `POST /users` → Create a new user
  - `GET /users` → List all users
  - `GET /users/{id}` → Retrieve a single user
  - `PUT /users/{id}` → Update user details
  - `DELETE /users/{id}` → Delete a user

- **Database Versioning with Alembic**
  - Version 1: Create `users` table
  - Version 2: Add `phone_number` and `address` columns

- **Security**
  - Sensitive info managed via `.env` file
  - Create a `.env` file in the root directory:
    
    ```bash
    DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost/fastapi_db
    ```
    
---

## Tech Stack

- **FastAPI** – Web framework for APIs
- **SQLAlchemy** – ORM for database operations
- **Alembic** – Database migration tool
- **PostgreSQL** – Relational database
- **pgAdmin 4** – Database management and inspection
- **Python 3.12+** – Project language

---
```

fastapi-alembic-project/
│
├─ alembic/
│   ├─ versions/          # Migration scripts
│   ├─ env.py
│   └─ README
├─ app/
│   ├─ main.py            # FastAPI entry point
│   ├─ models.py          # SQLAlchemy models
│   ├─ schemas.py         # Pydantic schemas
│   └─ database.py        # Database connection setup
├─ requirements.txt
├─ README.md
└─ alembic.ini

```
---

## Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/devxsam/fastapi-alembic-project.git
cd fastapi-alembic-project
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. Run Alembic migrations
```bash
alembic upgrade head
```

5. Start FastAPI server
```bash
uvicorn app.main:app --reload
```

6. Test the API

Open Swagger UI: http://127.0.0.1:8000/docs

