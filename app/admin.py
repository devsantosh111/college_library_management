from django.contrib import admin
from .models import Student, Book, Transaction, Burrowing, Report

# Register your models here.

admin.site.register([Student, Book, Transaction, Burrowing, Report])
