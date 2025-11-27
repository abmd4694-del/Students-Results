# Student Result Management System

A comprehensive Django-based student result management system with HTML/CSS/JS frontend.

## Features

- Student registration and management
- Course management
- Result entry and viewing
- Teacher/Admin authentication
- Search and filter functionality
- Responsive design

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### 2. Installation

```bash
# Navigate to the Django project directory
cd "django project1- result"

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (admin account)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

### 3. Access the Application

- **Main Application**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

### 4. Default Login

After creating a superuser, use those credentials to:

- Access the admin panel
- Login as a teacher to enter results

## Application Structure

- `results/` - Main application directory
  - `models.py` - Database models (Student, Course, Result, Teacher)
  - `views.py` - View functions for all pages
  - `urls.py` - URL routing
  - `admin.py` - Admin interface customization
  - `templates/` - HTML templates with embedded CSS/JS
  - `static/` - Static files (CSS, JS, images)

## Usage Guide

### For Admins/Teachers:

1. Login through the admin panel or login page
2. Add students, courses, and teachers
3. Enter student results for each course
4. View and manage all records

### For Students:

1. View results by searching with student ID or name
2. See all enrolled courses and grades
3. Check GPA and overall performance

## Features Overview

- **Dashboard**: Overview of system statistics
- **Student Management**: Add, edit, view, and delete students
- **Course Management**: Manage courses and subjects
- **Result Entry**: Enter marks and grades for students
- **Result Viewing**: Search and filter student results
- **Authentication**: Secure login for teachers and admins

## Deployment

### Vercel Deployment

This project is configured for deployment on Vercel.

1.  **Prerequisites**:

    - A GitHub account
    - A Vercel account

2.  **Steps**:

    - Push your code to a GitHub repository.
    - Log in to Vercel and click "Add New Project".
    - Import your GitHub repository.
    - Vercel should automatically detect the configuration from `vercel.json`.
    - Click "Deploy".

3.  **Environment Variables**:
    - If using a remote database (e.g., Neon, Supabase), configure the `DATABASE_URL` in Vercel's environment variables.
