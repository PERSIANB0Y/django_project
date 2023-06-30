from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Course(models.Model):
    student = models.ManyToManyField(Student)
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name
