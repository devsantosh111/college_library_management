from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/', views.api, name="api"),
    path('api/student/', views.get_students, name="getStudents"),
    path('api/student/<str:studentId>/', views.get_student, name="getStudents"),
    path('api/add/student/', views.add_student, name="addStudent"),
    path('api/update/student/<str:studentId>/',
         views.update_student, name="addStudent"),
    path('api/delete/student/<str:studentId>/',
         views.delete_student, name="addStudent"),
]
