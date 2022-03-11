## Description
Sample Djanogo app. Created Book Store Application to demonstrate basic Django concepts.

### Creating Project
django-admin startproject FirstDjangoSite

### Creating app inside project
django-admin startapp firstApp

### Running Server
python3 manage.py runserver

### Doing Migration (process of creating table out of Django models)
python3 manage.py makemigrations    #Checks if new models have been created
python3 manage.py migrate       # Creates actual tables out of models


### Django ORM (Used for adding data to database, kind of replacement for SQL queries

python3 manage.py shell # Open python shell which will use ORM to do CRUD on db

### Python script to check if there are any books(tables) created already and 
then create if not present
from myapp.models import Book
Book.objects.all() 
### Create book object
a = Book(name='This is book name', desc='Self help book', price=300)
a.save()

