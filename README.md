# pet-veterinary
Veterinary App using Django
This app contain a pet and  owner models. Including user register, user login, user logout and search functionality
pet model:
uses to register the pet's information including the owner of the pet
owner model:
uses to register the owner's information , without owner the app do not accept pet registeration.


# Dependencies used in the project:
Python 3.9.7
Django 3.2.7
# Project Setup:
Create virtual environment
Install dependencies
Execute the migrate process with python manage.py migrate
# Migrations for SQL:
Creating migration files: python manage.py makemigrations
The resulting files create the necessary tables in SQL database:  python manage.py migrate
# Run:
Run python manage.py runserver
# NOTE:
This app is for veterinary adminstrative use and every user(admin) can access and edit all pets and their owners.


