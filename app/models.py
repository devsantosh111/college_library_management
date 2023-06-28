from django.db import models

# Create your models here.

class Student(models.Model):
    studentId = models.CharField(max_length=50, primary_key=True)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField(unique=True)
    email = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    @property
    def fullName(self):
        return f"{self.firstName} {self.middleName or ''} {self.lastName}"
    
    @classmethod
    def generate_student_id(cls):
        prefix = "STD12310"
        count = cls.objects.count()
        return f"{prefix}{count + 1:04}"

    def __str__(self):
        return f"Student: {self.fullname}"
    

