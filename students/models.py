from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_phone_number = models.CharField(max_length=12)
    student_email = models.EmailField()
    student_city = models.CharField(max_length=100)
    student_course = models.CharField(max_length=100)
    student_age = models.IntegerField()
    
    def get_fields(self):
        return [(field.verbose_name, getattr(self, field.name)) for field in self._meta.fields]
    