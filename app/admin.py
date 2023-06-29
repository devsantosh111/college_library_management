from django.contrib import admin
from .models import Student, Book, Transaction

# Register your models here.

admin.site.register([Student, Book, Transaction])
