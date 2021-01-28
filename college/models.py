from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"| {self.first_name} {self.last_name} | {self.age} | {self.classroom} |"

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_joining = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"| {self.first_name} {self.last_name} | {self.date_of_joining} |"