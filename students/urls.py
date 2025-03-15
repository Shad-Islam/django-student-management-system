from django.urls import path
from .views import student_list, home, add_student, delete_student,view_student

urlpatterns = [
    path('', home, name='home'),
    path('student_list', student_list, name='student_list'),
    path('add_student', add_student, name='add_student'),
    path('delete_student/<int:student_id>',delete_student,name='delete_student'),
    path('view_student/<int:student_id>',view_student,name='view_student'),
]