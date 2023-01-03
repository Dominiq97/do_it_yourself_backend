# Elibrary - Online Library

#### CATANA Dominic Costin
#### CIUNGAN Diana Alexandra
#### IONESCU Sebastian Vlad
#### TRAISTARU Andreea Marilena

[![Python 9.6.3](https://img.shields.io/badge/python-3.9.6-blue.svg)]()
[![Django 3.1.1](https://img.shields.io/badge/django-3.1.1-blue.svg)]()
[![Django Rest Framework 3.11.1](https://img.shields.io/badge/djangorestframework-3.11.1-yellow.svg)]()
[![DRF-YASG 1.17.1](https://img.shields.io/badge/drf--yasg-1.17.1-red.svg)]()
[![PyJWT 2.6.0](https://img.shields.io/badge/PyJWT-2.6.0-orange.svg)]()

### mapping on elastic search
### Revise indices and mapping for next time
### add some data into elastic search to have something to work with

### using bulk api of elasticsearch
### ----------------------------------------
Our project consists of an online library with the following functionalities:

* for a user: <br>
·       search for books <br>
·       see all books <br>
* for an admin:  <br>
·       add books to the database <br>
·       delete books from the database <br>
·       update books from the database <br>
·       see all books <br>
·       search for books <br>


The data stored in the database is related to the books:<br>
o   name <br>
o   author<br>
o   publisher-address, name<br>
o   year<br>
o   stock<br>
o   price<br>
 
The user and the admin can search for books depending on their name or author or publisher <br>

RESTful API design:<br>
Search for books:<br>
 ```sh
  GET /api/v1/books
  GET /api/v1/books?title=TITLE
  GET /api/v1/books?author=AUTHOR
  GET /api/v1/books?publisher=PUBLISHER
  ```

Add book to database:
```
POST /api/v1/books/  //add book to database, where query is defined as a JSON with all the info packed with a header(Bearer <token>) to permit just the administrators to add books.
```
Delete book from database:
```
DELETE /api/v1/books/{id} //delete a book based on id
```
Update book from database
```
PUT /api/v1/books/{id} – update/resave() an entire book based on id
PATCH /api/v1/books/{id} – update the object with a few changed attribute’s value book based on id
```

Create admin account
```
POST /api/v1/administrators 
```

Create customer account
```
POST /api/v1/customers
GET  /api/v1/customers <- get list of all customers
```

## Installation Instructions
### Just like that: <br>

Create your own virtual environment : <br>
`python -m venv venv`

Activate the environment : <br>
`venv\Scripts\activate`

Then install the requirements : <br>
`pip install -r requirements.txt`

And migrate the models into the database(SQLite): <br>
`python manage.py migrate`

You're ready to go!! <br>
`python manage.py runserver`
