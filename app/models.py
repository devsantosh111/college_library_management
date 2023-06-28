from django.db import models
from datetime import timedelta

# Create your models here.

class Student(models.Model):
    studentId = models.CharField(max_length=50, primary_key=True)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=20, unique=True)
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
    status = models.CharField(max_length=1, choices=BookStatus.choices, default=BookStatus.AVAILABLE)
    isbn = models.CharField(max_length=(50), unique=True)

    def __str__(self):
        return f"Book: {self.title}"

class Transaction(models.Model):
    transactionId = models.AutoField(primary_key=True)
    studetnId = models.ForeignKey(Student, on_delete=models.CASCADE)


class Burrowing(models.Model):
    burrowingId = models.AutoField(primary_key=True)
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)


class Report(models.Model):
    reportId = models.AutoField(primary_key=True)
    transactionId = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    burrowingId = models.ForeignKey(Burrowing, on_delete=models.CASCADE)
    transactionDate = models.DateField(auto_now_add=True, unique=True)
    returnDate = models.DateField()

    def save(self, *args, **kwargs):
        if not self.reportId and not self.returnDate:
            self.returnDate = self.transactionDate + timedelta(days=14)
        return super().save(*args, **kwargs)




    

