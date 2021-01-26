from django.shortcuts import render
from college.models import Student, Teacher

def index(request):
    students=Student.objects.all()
    teachers=Teacher.objects.all()

    return render(request, 'college/index.html', context={
        'students': students
    })
