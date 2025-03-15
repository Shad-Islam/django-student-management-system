from django.urls import path
from .views import student_list, home, add_student

urlpatterns = [
    path('', home, name='home'),
    path('student_list', student_list, name='student_list'),
    path('add_student', add_student, name='add_student'),
]