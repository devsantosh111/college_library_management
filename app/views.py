from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to student management api"})

@api_view(["GET"])
def api(request):
    return Response({"endpoints": "detail"})

@api_view(["GET"])
def get_students(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_student(request, studentId):
    student = Student.objects.get(studentId = studentId)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


