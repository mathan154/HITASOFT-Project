# HITASOFT Task Management System 

## Overview
This is a simple Task Management System built using Django and Django REST Framework (DRF). It supports user registration, login, token-based authentication, and full CRUD operations for tasks, along with filtering and sorting features.

---

## Prerequisites

Ensure you have the following installed:
- Python 3.10+
- pip (Python package manager)
- virtualenv (optional but recommended)

---

## Project Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
Create a `requirements.txt` file with the following:
```txt
Django==5.2
djangorestframework==3.15.1
djangorestframework-authtoken==1.3.0
```
Then install:
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

---

## API Endpoints & Usage

### 1. User Registration
- **Method**: POST  
- **URL**: `http://127.0.0.1:8000/register/`  
- **Body (JSON)**:
```json
{
  "username": "maxaa",
  "password": "B#dgfy12458509"
}
```

### 2. User Login
- **Method**: POST  
- **URL**: `http://127.0.0.1:8000/login/`  
- **Body (JSON)**:
```json
{
  "username": "maxaa",
  "password": "B#dgfy12458509"
}
```
- **Response**:
```json
{
  "message": "Login successful. Hello maxaa!",
  "token": "your_token_here"
}
```

Use the token in headers for all protected requests:
```
Authorization: Token your_token_here
```

### 3. Task Endpoints

#### 3.1 List All Tasks
- **Method**: GET  
- **URL**: `http://127.0.0.1:8000/tasks/`

#### 3.2 Create Task
- **Method**: POST  
- **URL**: `http://127.0.0.1:8000/tasks/`  
- **Body**:
```json
{
  "title": "New Feature",
  "description": "Implement GraphQL support",
  "priority": "Medium",
  "status": "Ongoing",
  "due_date": "2025-04-15"
}
```

#### 3.3 Retrieve Specific Task
- **Method**: GET  
- **URL**: `http://127.0.0.1:8000/tasks/{id}/`

#### 3.4 Update Task
- **Method**: PUT  
- **URL**: `http://127.0.0.1:8000/tasks/{id}/`

#### 3.5 Delete Task
- **Method**: DELETE  
- **URL**: `http://127.0.0.1:8000/tasks/{id}/`

### 4. Filtering and Sorting

#### 4.1 Sorting by Priority
- URL: `http://127.0.0.1:8000/tasks/?ordering=priority`
- Descending: `?ordering=-priority`
- You can also sort by `due_date`, `status`

#### 4.2 Search by Keyword
- URL: `http://127.0.0.1:8000/tasks/?search=urgent`
- Fields: `title`, `description`, `priority`, `status`



---

## Notes
- Password must meet Django’s validation rules.
- Token must be included in the headers for all task operations.
- Use Postman or similar tools to test API endpoints easily.

---

## License
This project is licensed for HITASOFT internal development and educational purposes.

