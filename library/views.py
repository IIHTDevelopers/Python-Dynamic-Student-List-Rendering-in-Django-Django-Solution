from django.shortcuts import render
from .models import Student

def student_list_view(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})
