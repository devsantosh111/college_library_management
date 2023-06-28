from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/', views.api, name="api"),
    path('api/student/', views.get_students, name="getStudents"),
    path('api/student/<str:studentId>/', views.get_student, name="getStudents")
]