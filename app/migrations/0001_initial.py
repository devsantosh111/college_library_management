# Generated by Django 4.2.2 on 2023-06-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(blank=True, max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
