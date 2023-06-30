from django.contrib import admin

# Register your models here.

from main2.models import Course , Student

admin.site.register(Course)
admin.site.register(Student)
