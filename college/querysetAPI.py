# QuerySet API Related methods and field lookups
from college.models import Student, Teacher
from django.db.models import Q, Count


def method_returning_new_queryset(request):
    ''' Methods when applied to a queryset will return a new queryset '''
    students_queryset = Student.objects # objects is the default model manager and returns a queryset
    teachers_queryset = Teacher.objects

    # all()--> returns a copy of current queryset
    queryset_all = students_queryset.all()

    # distinct()--> returns a new QuerySet that uses SELECT DISTINCT in its SQL query.
    queryset_distinct = students_queryset.distinct()

    # filter()--> returns a new QuerySet containing objects that match the given lookup parameters
    queryset_filter = students_queryset.filter(age=26)

    # exclude()--> returns a new queryset with objects excluding the kwargs in arguements
    queryset_exclude = students_queryset.exclude(age=26) # will not return where age is 26

    # difference()--> returns a new queryset with objects that does not exists between the given querysets
    queryset_1 = students_queryset.values_list('first_name','last_name')
    queryset_2 = teachers_queryset.values_list('first_name','last_name')
    queryset_difference = queryset_1.difference(queryset_2)

    # intersection()--> returns a new queryset with objects common in given querysets
    queryset_intersection = queryset_1.intersection(queryset_2)

    # union()--> makes a union among all the querysets| returns a new querset
    queryset_union = queryset_1.union(queryset_2)

    # values()--> returns a QuerySet that returns dictionaries, rather than model instances
    queryset_values = students_queryset.values()

    # values_list()--> returns a tuple of the columns/attributes passed as arguements
    queryset_values_list = students_queryset.values_list('first_name','last_name', named=True) # will return namedTuple

    # using()--> using which database(as defined in setting file)
    queryset_using = students_queryset.using('default') # default is name of sqlite3 db in settings.py

    # dates()--> returns a list of all possible matches of date pattern provided
    querset_dates = teachers_queryset.dates('date_of_joining', 'year') # will return dates in year format 

    # annotate()--> returns a query with the parameter applied on each object
    queryset_annotate = students_queryset.annotate(count_first_name=Count('first_name'))
    # queryset_annotate.count_first_name() # will return the total count
    queryset_annotate[0].count_first_name # will return the count per object

    # order_by()--> returns a queryset with the ordered objects as parameterized 
    queryset_order_by = students_queryset.order_by('last_name','-age') # order asc by last_name, desc by age

    # reverse()--> returns the reversed order of objects|objects must be ordered first either in Meta class or by order_by
    queryset_reverse = queryset_order_by.reverse() # since this is already ordered

    # none()--> returns empty queryset| is an instance of EmptyQuerySet(django.db.models.query)
    queryset_none = students_queryset.none()

    # raw()--> takes a raw SQL query & returns a django.db.models.query.RawQuerySet instance.
    queryset_raw = students_queryset.raw('SELECT * FROM college_student') # app_modelname-in lowercase

    return {
        'queryset_all': queryset_all, 
        'queryset_distinct': queryset_distinct,
        'queryset_filter': queryset_filter,
        'queryset_exclude': queryset_exclude, 
        'queryset_difference': queryset_difference, 
        'queryset_intersection': queryset_intersection, 
        'queryset_union': queryset_union, 
        'queryset_values': queryset_values, 
        'queryset_values_list': queryset_values_list,
        'queryset_using': queryset_using,
        'querset_dates': querset_dates,
        'queryset_annotate': queryset_annotate,
        'queryset_order_by': queryset_order_by,
        'queryset_reverse': queryset_reverse,
        'queryset_none': queryset_none,
        'queryset_raw': queryset_raw,
    } # returning context as context dictionary object

def method_not_returning_new_queryset(request):
    # get() --> returns single object matching parameter| returns error--> DoesNotExis & MultipleObjectsReturned
    result_get = Student.objects.get(first_name='Komal')

    # create()--> creates an object and saves it in one step.
    result_create = Student.objects.create(first_name='Shivani', last_name='Sharma', age=26, classroom='IT')

    # get_or_create()--> returns object & boolean indicating if new object is created or retrieved
    result_get_or_create = Student.objects.get_or_create(first_name='Komal',last_name='Rathi', age=24, classroom='CS')

    # update_or_create()--> returns object & boolean indicating if object is created or updated
    result_update_or_create = Student.objects.update_or_create(first_name='Komal',last_name='Rathi', age=24, classroom='CS',
                                defaults={'last_name': 'Dahiya'} # defaults dict data is updated
                            )
    
    # bulk_create()--> create objects in bulk from the list
    result_bulk_create = Teacher.objects.bulk_create([
                                                    Teacher(first_name='David', last_name='Milan'), 
                                                    Teacher(first_name='Sushil',last_name='Tyagi'),
                                                    Teacher(first_name='First', last_name='Last'),
                        ])

    # update()--> returns no of updated records 
    result_update = Teacher.objects.filter(first_name='First', last_name='Last').update(first_name='Neetu', last_name='Singh')

def queryset_field_lookup(request):
    pass



## Put the below code somewhere
# students = Student.objects.all()
# # OR query using Q objects
# students = Student.objects.filter(
#     Q(age__lte=25) | Q(first_name__startswith='Vinay') | ~Q(classroom__startswith='CS')
# )

# # And query using Q object
# students = Student.objects.filter(
#     Q(last_name__contains='Rathi') & Q(age__gt=23)
# )

# # A union query on students and teachers queryset
# students_query = Student.objects.values_list('first_name','last_name')
# teachers_query = Teacher.objects.values_list('first_name','last_name')
# union_queryset = students_query.union(teachers_query)
