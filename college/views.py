from django.shortcuts import render
from college.models import Student, Teacher
from django.db.models import Q

def index(request):
    students = Student.objects.all()
    # OR query using Q objects
    students = Student.objects.filter(
        Q(age__lte=25) | Q(first_name__startswith='Vinay') | ~Q(classroom__startswith='CS')
    )

    # And query using Q object
    students = Student.objects.filter(
        Q(last_name__contains='Rathi') & Q(age__gt=23)
    )

    # A union query on students and teachers queryset
    students = Student.objects.values_list('first_name')
    teachers = Teacher.objects.values_list('first_name')
    union_queryset = students.union(teachers)

    return render(request, 'college/index.html', context={
        'students': students,
        'union_queryset': union_queryset,
    })
