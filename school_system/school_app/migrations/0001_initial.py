# Generated by Django 5.0.7 on 2024-07-22 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_code', models.CharField(max_length=50, unique=True)),
                ('delivery_mode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('role', models.IntegerField(choices=[(1, 'Staff'), (2, 'Admin')])),
                ('active_user', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('role', models.IntegerField(choices=[(1, 'Student'), (2, 'Admin')])),
                ('active_user', models.BooleanField(default=True)),
                ('courses', models.ManyToManyField(related_name='students', to='school_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.course')),
                ('absent_students', models.ManyToManyField(related_name='absences', to='school_app.student')),
                ('attended_students', models.ManyToManyField(related_name='attendances', to='school_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=200)),
                ('activity_date', models.DateField()),
                ('students', models.ManyToManyField(related_name='activities', to='school_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('role', models.IntegerField(choices=[(1, 'Teacher'), (2, 'Admin')])),
                ('active_user', models.BooleanField(default=True)),
                ('teaching_course', models.ManyToManyField(related_name='teachers', to='school_app.course')),
            ],
        ),
    ]
