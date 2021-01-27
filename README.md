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
>>> Student.objects.filter(
    Q(last_name__contains='Rathi') & Q(age__gt=23)
    )
```

## Make a 'Union' query on two querysets
A union query needs to have same columns in the querysets on which the union is applied. <br>
The UNION operator selects only distinct values by default. To allow duplicate values, use the all=True argument.
```python
>>> student_query = Student.objects.values_list('first_name')
>>> teacher_query = Teacher.objects.values_list('first_name')
>>> union_query = student_query.union(teacher_query)
```

## Exclude query in Django
```python
>>> Student.object.exclude(age=20)
>>> Student.object.filter(~Q(age=20))
```

## Methods that return new QuerySets
|  |  |  |
| :-----:|:-------:| --------:| 
| filter | exclude | annotate |
| order_by | reverse | distinct |
| values | values_list | dates |
| datetimes | none | all |
| union | intersection | difference |
| select_related | prefetch related | extra |
| defer | only | using |
| select_for_update | raw | |
