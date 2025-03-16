from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages


# Create your views here.
def student_list(request):
    students = Student.objects.all()
    # print(students)
    # result = ""
    # for student in students:
    #     result += f"name: {student.student_name} <br> roll number: {student.student_roll} <br> city: {student.student_city} <br> college name: {student.student_college} <br> age: {student.student_age} <br> <br>"
        
    # return HttpResponse(result)
    
    return render(request, "student_list.html" ,{'students': students})


def home(request):
    return render(request, "base.html")

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student added successfully')
            return redirect('add_student')
        return render(request, "add_student.html",{'form': form})
            
    
    else:
        form = StudentForm()
    return render(request, "add_student.html",{ 'form': form})



def  delete_student(request, student_id):
        student = Student.objects.get(id=student_id)
        student.delete()
        messages.add_message(request, messages.SUCCESS, 'Student deleted successfully')
        return redirect('student_list')

def view_student(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request,"view_student.html",{'student': student})

def edit_student(request,student_id):
    student = Student.objects.get(id = student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student updated successfully')
            return redirect('student_list')
        return render(request, "edit_student.html",{'form': form ,'student': student})
    else:
        form = StudentForm(instance=student)
    return render(request, "edit_student.html",{'form': form ,'student': student})