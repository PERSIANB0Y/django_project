from django.shortcuts import render

# Create your views here.

from main2.models import Course, Student
from .forms import studentform


def Courselist(request):
    list = Course.objects.all()
    return render(request, 'html.html', {"classes": list})


def Studentlist(request):
    list = students = Student.objects.all()
    return render(request, 'html.html', {"student": list})


def signup(request):
    error = []
    if request.POST:
        a = studentform(request.POST, request.FILES)
        if a.is_valid():
            a.save()
        else:
            error = a.errors

    form = studentform
    return render(request, "signup.html", {'form': form, "error": error})
