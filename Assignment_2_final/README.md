**Student Management System using Django**

**OVERVIEW:** 
This project is a Student Management System built with Django. It allows users to manage student records, including adding, editing, and deleting students, as well as searching and paginating student records. Only authenticated users can perform actions on student records.

**Features:**
Add, edit, and delete student records.
Search students by name.
Pagination on student list page.
User authentication: Only authenticated users can manage student records.
Form validation for email and grade fields.

**Requirements:**
Python 3.8+
Django 3.2+
Virtual environment (recommended)

**Setup Instructions:**
Step 1: Clone the repository
---- git clone <your-repository-url>
----- cd student_management

Step 2: Set up a virtual environment
---- python3 -m venv venv
 Activate the virtual environment:
   ---- venv\Scripts\activate
   
Step 3: Install Django
---- python -m pip install Django

Step 4: Set up the database
---- python manage.py makemigrations
---- python manage.py migrate

Step 5: Create a superuser
---- python manage.py createsuperuser

Step 6: Run the development server
---- python manage.py runserver

Step 7: Access the admin panel
To manage students through the admin panel, go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

**Usage:**
Admin Panel: Access at http://127.0.0.1:8000/admin/ (login required).
Add/Edit Student: Navigate to the students page to add new student records or edit existing ones.
Search: Use the search bar on the student list page to find students by first or last name.
Pagination: Browse through students with a paginated view (10 records per page).

**Validation:**
The email field is validated to ensure uniqueness.
The grade field must be between 1 and 12.

**Authentication:**
Only authenticated users can add, edit, or delete student records.
Log in to access these features.

**Project Structure:**
students/models.py: Defines the Student model.
students/forms.py: Contains the forms for adding and editing students.
students/views.py: Handles the logic for listing, adding, and editing students.
students/templates/: Contains the HTML templates for the views.

This README.md provides all the essential setup steps and usage instructions for running the Student Management System project locally.
