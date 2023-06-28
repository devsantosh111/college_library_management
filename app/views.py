from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to student management api"})

@api_view(["GET"])
def api(request):
    return Response({"endpoints": "detail"})

@api_view(["GET"])
def get_students(request):
    return Response({"message": "Welcome to student management api"})


