# Django Quora Clone 📝

A simple Quora-like web application built with Django and Django Forms (no DRF).  
Users can register, log in, post questions, view questions, write answers, and like answers.


## Features 🚀

- User Registration & Login
- Post Questions
- View All Questions
- Answer Questions
- Like Answers
- Logout


## Setup Instructions 🛠️

Follow these steps to run the project locally.

### 1. Clone the repository
      git clone https://github.com/your-username/django-quora-clone.git
      
### 2. Create virtual environment
      python -m venv env
      source env/bin/activate
      
### 3. install dependency
      pip install -r requirements.txt

### 4. Run migrations
      python manage.py makemigrations
      python manage.py migrate

### 5. Run the development server
      python manage.py runserver

**folder structure**
```
Quara/                  # Main project directory
├── Quara/              # Django project settings directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── config.ini
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── quara/              # Django app directory (your main app)
│   ├── migrations/     # Migration files (DB schema)
│   │   └── __init__.py
│   │
│   ├── templates/      # HTML Templates
│   │   └── (your HTML files will go here)
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py        # Your Django forms
│   ├── models.py
```
**URL**
  - http://127.0.0.1:8000/post-question/
  
  - http://127.0.0.1:8000/login/
  
  - http://127.0.0.1:8000/question/3/
  
  - http://127.0.0.1:8000/post-question/

  - http://127.0.0.1:8000/signup/

  - http://127.0.0.1:8000/ 
