# QuerySet API Related methods and field lookups
from college.models import Student, Teacher
from django.db.models import Q


def method_returning_new_queryset(request):
    pass

def method_not_returning_new_queryset(request):
    pass

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
