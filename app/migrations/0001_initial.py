# Generated by Django 4.2.2 on 2023-06-29 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70, unique=True)),
                ('status', models.CharField(choices=[('A', 'Available'), ('L', 'Loaned'), ('R', 'Returned'), ('D', 'Due Date Passed'), ('O', 'Overdue'), ('B', 'Borrower Notified'), ('I', 'Received from Library'), ('X', 'Discarded by Librarian'), ('S', 'Sold to Customer'), ('C', 'Incorrectly Received'), ('M', 'Missing in the library'), ('N', 'Not Available at this time.'), ('U', 'Unknown Status')], default='A', max_length=1)),
                ('isbn', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(blank=True, max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('reportId', models.AutoField(primary_key=True, serialize=False)),
                ('transactionDate', models.DateField(auto_now_add=True, unique=True)),
                ('returnDate', models.DateField(blank=True)),
                ('bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
