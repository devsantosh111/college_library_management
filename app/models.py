from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class Student(models.Model):
    studentId = models.CharField(max_length=50, primary_key=True, blank=True)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    @property
    def fullName(self):
        if self.middleName:
            return f"{self.firstName} {self.middleName} {self.lastName}"
        return f"{self.firstName} {self.lastName}"

    @classmethod
    def generate_student_id(cls):
        prefix = "STD12310"
        count = cls.objects.count()
        return f"{prefix}{count + 1:04}"

    def save(self, *args, **kwargs):
        if not self.studentId:
            self.studentId = self.__class__.generate_student_id()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Student: {self.fullName}"


class BookStatus(models.TextChoices):
    AVAILABLE = 'A', 'Available'
    LOANED = 'L', 'Loaned'
    RETURNED = 'R', 'Returned'
    DUE = 'D', 'Due Date Passed'
    OVERDUE = 'O', 'Overdue'
    BORROWER_NOTIFIED = 'B', 'Borrower Notified'
    RECEIVED = 'I', 'Received from Library'
    DISCARDED = 'X', 'Discarded by Librarian'
    SOLD = 'S', 'Sold to Customer'
    INCORRECTLY_RECEIVED = 'C', 'Incorrectly Received'
    MISSING = 'M', 'Missing in the library'
    NOT_AVAILABLE = 'N', 'Not Available at this time.'
    UNKNOWN = 'U', 'Unknown Status'


class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70, unique=True)
    status = models.CharField(
        max_length=1, choices=BookStatus.choices, default=BookStatus.AVAILABLE)
    isbn = models.CharField(max_length=(50), unique=True)

    def __str__(self):
        return f"Book: {self.title}"


class Transaction(models.Model):
    reportId = models.AutoField(primary_key=True)
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    transactionDate = models.DateField(blank=True, unique=True)
    returnDate = models.DateField(blank=True)

    def save(self, *args, **kwargs):
        if not self.transactionDate and not self.returnDate:
            self.transactionDate = datetime.now()
            self.returnDate = self.transactionDate + timedelta(days=14)
        return super().save(*args, **kwargs)
