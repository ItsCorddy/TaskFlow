
# TaskFlow

TaskFlow is a web-based Student Task Management System
developed using Python and Django.

## Live Website

https://taskflowstudent.pythonanywhere.com

## Project Objective

To help students organize academic tasks, manage deadlines,
prioritize responsibilities and monitor their productivity.

## Features

- User registration and authentication
- Create, read, update and delete tasks
- Task priorities and deadlines
- Task search and filtering
- Progress tracking
- Overdue task detection
- Django administration panel
- JSON API
- Online deployment

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite
- PythonAnywhere

## Local Installation

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   pip install -r requirements.txt

4. Generate a local secret key:

   python -c "from django.core.management.utils import get_random_secret_key; from pathlib import Path; Path('.taskflow_secret').write_text(get_random_secret_key())"

5. Apply database migrations:

   python manage.py migrate

6. Start the development server:

   python manage.py runserver

7. Open http://127.0.0.1:8000/

## Architecture

TaskFlow follows Django's Model-View-Template (MVT)
architecture.

## Purpose

Developed as an individual semester project for
web development with Python and Django.
