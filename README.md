# Django-ORM(Object Relation Mapper)

## What are the uses of an ORM?
- An ORM enables the developer to write the database queries in the backend language. 
- Can easily switch between any relational database i.e., MySQL to PostgreSQL
- Additional features out of box like

## What is a Q object in Django ORM?
A Q() object, like an F object, encapsulates a SQL expression in a Python object that can be used in database-related operations.

## How to make an OR query using Q object?
General way to execute an OR query(where first_name starts with 'Vinay' or 'Vijay')
```python
>>> Student.objects.filter(first_name__startswith='Vijay')|Student.objects.filter(first_name__startswith='Vinay')
```
Executing with the Q objects.
```python

```
