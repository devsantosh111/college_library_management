from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/', views.api, name="api"),
    path('api/students/', views.get_students, name="getStudents")
]