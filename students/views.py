from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()
    # print(students)
    # result = ""
    # for student in students:
    #     result += f"name: {student.student_name} <br> roll number: {student.student_roll} <br> city: {student.student_city} <br> college name: {student.student_college} <br> age: {student.student_age} <br> <br>"
        
    # return HttpResponse(result)
    
    return render(request, "student_list.html" ,{'students': students})
    