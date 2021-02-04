# Django-ORM(Object Relation Mapper)

## What are the uses of an ORM?
- An ORM enables the developer to write the database queries in the backend language. 
- Can easily switch between any relational database i.e., MySQL to PostgreSQL
- Additional features out of box like

## Example of available ORMs

## QuerySet in Django
A QuerySet represents a collection of objects from your database. In SQL terms, a QuerySet equates to a SELECT statement. You get a QuerySet by using your model’s Manager. Each model has at least one Manager, and it’s called objects by default. 
```python
Students.objects
# <django.db.models.manager.Manager object at 0x7f4bda75b7c0>
```

## What is a Q object in Django ORM?
A Q() object is an object used to encapsulate a collection of keyword arguements. 
```python
from django.db.models import Q
Q(question__startswith='Who') | Q(question__startswith='What')
```

## How to make an OR query using Q object?
General way to execute an OR query(where first_name starts with 'Vinay' or 'Vijay')
```python
Student.objects.filter(first_name__startswith='Vijay')| \
Student.objects.filter(first_name__startswith='Vinay')
```
Executing with the Q objects.
```python
Student.objects.filter(Q(first_name__startswith='Vijay') | Q(first_name__startswith='Vinay'))
```
## Make an 'and' query using Q object.
```python
Student.objects.filter(Q(last_name__contains='Rathi') & Q(age__gt=23))
```

## What is an F object in Django ORM?
An F() object represents the value of a model field or annotated column. An F objects helps me performing operation on value without having it pulled into Python memory
```
>>> from college.models import Student
>>> from django.db.models import F
>>> student = Student.objects.get(pk=22)
>>> student
<Student: | Komal Dahiya | 24 | CS |>
>>> student.age = F('age')+1
>>> student
<Student: | Komal Dahiya | F(age) + Value(1) | CS |>
>>> student.save()
>>> student
<Student: | Komal Dahiya | F(age) + Value(1) | CS |>
>>> student_new = Student.objects.get(pk=22)
>>> student_new
<Student: | Komal Dahiya | 25 | CS |>
>>> student.age
<CombinedExpression: F(age) + Value(1)>
```

## Make a 'Union' query on two querysets
A union query needs to have same columns in the querysets on which the union is applied. <br>
The UNION operator selects only distinct values by default. To allow duplicate values, use the all=True argument.
```python
student_query = Student.objects.values_list('first_name')
teacher_query = Teacher.objects.values_list('first_name')
union_query = student_query.union(teacher_query)
```

## Exclude query in Django
```python
Student.objects.exclude(age=20)
Student.objects.filter(~Q(age=20))
```

## Methods that return new QuerySets
|        |         |         |         |         |         |         |         |
| :-----:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| difference   | exclude | using | distinct  | order_by | none  | all | prefetch_related  |
| values_list  | values  | dates | datetimes | union    | only  | raw | select_related    |
| intersection | filter  | extra | annotate  | reverse  | defer |     | select_for_update |

Note: extra() is going to be deprecated at some point in the future. <br>
datetimes() is similar to dates but with extra times filtering capacity <br>
defer() defers the load of field(s) passed as args until you don't need them to optimize. <br>
only() does opposite to defer & loads field(s) passed as args immediately, defers all other fields


## Methods that do not return new QuerySets
|        |         |         |         |         |         |         |         |         |
| :-----:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| get  | create  | get_or_create    | bulk_create | count | aggregate | in_bulk | update | explain  |
| last | latest  | update_or_create | bulk_update | first | earliest  | exists  | delete | iterator |

Note: bulk_update() is similar to bulk_create but with update capabalities

## Field lookups in queryset
|        |         |         |         |       |         |         |         |
| :-----:|:-------:|:-------:|:-------:|:-----:|:-------:|:-------:|:-------:|
| exact | iexact | contains | icontains | in | gt | gte | lt | lte | range |
| startswith | istartswith | endswith | iendswith | date | year | iso_year | month | day | week |
| week_day | quarter | time | hour | minute | isnull | regex | iregex |

Note: SQLite doesn’t support case-sensitive LIKE statements; contains acts like icontains for SQLite. <br>
date :: For datetime fields, casts the value as date.
