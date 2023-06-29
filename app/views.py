from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from .utils import check_required_fields

# Create your views here.


@api_view(["GET"])
def home(request):
    try:
        return Response({"detail": "Welcome to College Library Management API"})
    except Exception as e:
        return Response({"detail": str(e)}, status=500)


@api_view(["GET"])
def api(request):
    try:
        return Response({
            "ENDPOINTS": "DETAILS",
            "/": {
                        "method": "GET",
                        "body": None,
                        "description": "Returns welcome message"
                        },
            "api/": {
                "method": "GET",
                "body": None,
                "description": "Returns api endpoints and its details"
            },
            "api/student/": {
                "method": "GET",
                "body": None,
                "description": "Returns record of students"
            },
            "api/student/<str:id>/": {
                "method": "GET",
                "body": None,
                "description": "Returns a specific student's data by id"
            },
            "api/add/student/": {
                "method": "POST",
                "body": {"firstName": "str", "middleName": "optional|str", "lastName": "str", "age": "int", "contact": "str", "email": "str", "address": "str"},
                "description": "Adds new records in the database"
            },
            "api/update/student/<str:studentId>/": {
                "method": "PUT",
                "body": {"firstName": "str", "middleName": "optional|str", "lastName": "str", "age": "int", "contact": "str", "email": "str", "address": "str"},
                "description": "Updates existing records from the database"
            },
            "api/delete/<str:studentId>/": {
                "method": "DELETE",
                "body": None,
                "description": "Deletes an entry with given ID"
            },
        })
    except Exception as e:
        return Response({"detail": str(e)}, status=500)


@api_view(["GET"])
def get_students(request):
    try:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"detail": str(e)}, status=500)


@api_view(["GET"])
def get_student(request, studentId):
    try:
        student = Student.objects.get(studentId=studentId)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"detail": "Student data doesnot exist."}, status=404)
    except Exception:
        return Response({"detail": "An error occurred."}, status=500)


@api_view(["POST"])
def add_student(request):
    try:
        # Perform data validation
        data = request.data
        required_fields = ['firstName', 'lastName',
                           'email', 'contact', 'age', 'address']
        check_required_fields(data, required_fields)
        studentObj = Student(**data)
        studentObj.save()
        return Response({"detail": f"{str(studentObj)} added successfully to database"})
    except KeyError as e:
        return Response({"detail": f"Missing required field {str(e)}"}, status=400)
    except ValidationError as e:
        return Response({"detail": str(e)}, status=400)
    except ValueError:
        return Response({"detail": "Invalid data"}, status=400)
    except Exception:
        return Response({"detail": "An error occurred."}, status=500)


@api_view(["PUT"])
def update_student(request, studentId):
    try:
        student = Student.objects.get(studentId=studentId)
        data = request.data
        serializer = StudentSerializer(instance=student, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"detail": "Student data has been updated successfully"})
    except Student.DoesNotExist:
        return Response({"detail": "Student data doesnot exist."}, status=404)
    except KeyError as e:
        return Response({"detail": f"Missing required field {str(e)}"}, status=400)
    except ValidationError as e:
        return Response({"detail": str(e)}, status=400)
    except Exception as e:
        return Response({"detail": str(e)}, status=500)


@api_view(["DELETE"])
def delete_student(request, studentId):
    try:
        student = Student.objects.get(studentId=studentId)
        student.delete()
        return Response({"detail": "Student data deleted successfully"})
    except Student.DoesNotExist:
        return Response({"detail": "Student data doesnot exist."}, status=404)
    except Exception:
        return Response({"detail": "An error occurred."}, status=500)
    
