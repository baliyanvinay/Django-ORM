# Django-ORM(Object Relation Mapper)

## What are the uses of an ORM?
- An ORM enables the developer to write the database queries in the backend language. 
- Can easily switch between any relational database i.e., MySQL to PostgreSQL
- Additional features out of box like

## What is a Q object in Django ORM?
A Q() object is an object used to encapsulate a collection of keyword arguements. 
```python
from django.db.models import Q
Q(question__startswith='Who') | Q(question__startswith='What')
```

## How to make an OR query using Q object?
General way to execute an OR query(where first_name starts with 'Vinay' or 'Vijay')
```python
>>> Student.objects.filter(first_name__startswith='Vijay')|Student.objects.filter(first_name__startswith='Vinay')
```
Executing with the Q objects.
```python
>>> Student.objects.filter(
    Q(first_name__startswith='Vijay') | Q(first_name__startswith='Vinay')
    )
```
## Make an 'and' query using Q object.
```python
>>> 
```