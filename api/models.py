from django.db import models
from django.contrib.auth.models import AbstractUser


class Class(models.Model):
    name = models.CharField(max_length=255)


class Modul(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Teacher(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Django'ning o'zida parolni boshqarish # noqa
    class_name = models.ManyToManyField('Modul', related_name='teacher')

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    great = models.CharField(max_length=5, null=True, blank=True, default=None)  # default null
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE,
                                   related_name='students')  # ForeignKey orqali bog'lash # noqa
    moduls = models.ManyToManyField('Modul', related_name='students')  # Many-to-Many bog'lanish Modullar bilan # noqa

    def __str__(self):
        return self.full_name


class Lesson(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255, null=True, blank=True)
    students = models.ManyToManyField(Student, related_name='lessons')  # students list
    moduls = models.ManyToManyField(Modul, related_name='lessons')  # get post

    def __str__(self):
        return f"Lesson on {self.date}"
