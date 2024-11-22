# Spy-Cat-Agency 

This is a Django REST Framework-based application for managing spy cats, their missions, and associated targets.
The application demonstrates CRUD functionality, integration with a third-party API for cat breed validation, and optimized database queries.

## Features
- Manage Spy Cats: Add, update, delete, and list spy cats.
- Manage Missions: Assign missions to cats, create targets, and update progress.
- Optimized database performance using select_related and prefetch_related.
- Automatic API documentation using Swagger.
- Validation of cat breeds via TheCatAPI.

## Installation

### 1. Clone the Repository
```shell
git clone https://github.com/Alexandr-Politov/Spy-Cat-Agency.git
cd spy_cat_agency
```
### 2. Set Up a Virtual Environment
```shell
python -m venv venv
source venv/bin/activate       # On Linux/MacOS
venv\Scripts\activate          # On Windows
```
### 3. Install Dependencies
```shell
pip install -r requirements.txt
```
### 4. Apply Migrations
Run the following commands to set up the database:
```shell
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the Django development server:
```shell
python manage.py runserver
```
### Access the application:
- API Endpoints: http://127.0.0.1:8000/api/
- Swagger Documentation: http://127.0.0.1:8000/swagger/
- Admin Panel: http://127.0.0.1:8000/admin/
