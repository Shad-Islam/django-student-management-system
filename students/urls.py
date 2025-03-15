from django.urls import path
from .views import student_list, home

urlpatterns = [
    path('', home),
    path('student_list', student_list, name='student_list'),
]