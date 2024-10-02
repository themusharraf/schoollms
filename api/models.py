from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseDate(models.Model):
    """created va updated date ma'lumotlarini saqlash uchun abstract model"""
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Class(BaseDate):
    name = models.CharField(max_length=255)


class Science(BaseDate):
    """Fanlar uchun model"""
    name = models.CharField(max_length=255)


class Modul(BaseDate):
    """Fanlarning modullarini saqlash uchun model"""
    name = models.CharField(max_length=255)
    science = models.ForeignKey(Science, related_name='moduls', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(AbstractUser):
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


class Lesson(BaseDate):
    """Darslar uchun model"""

    modul = models.ForeignKey(Modul, related_name='lessons', on_delete=models.PROTECT)  # get post
    name = models.CharField(max_length=255, null=True, blank=True)
    lesson_text = models.TextField()

    students = models.ManyToManyField(Student, related_name='lessons')  # students list

    def __str__(self):
        return f"Lesson on {self.date}"


class LessonSubmission(BaseDate):
    """Darslarda o'quvchilarni baholash uchun model"""

    student = models.ForeignKey(Student, related_name='grades',
                                on_delete=models.PROTECT)  # 1 ta student uchun 1 ta baho
    grade = models.CharField(max_length=5, null=True, blank=True, default=None)
    lesson = models.ForeignKey(Lesson, related_name='grades', on_delete=models.PROTECT)  # get post

    def __str__(self):
        return f"{self.lesson.id} > {self.student.full_name} > {self.grade}"
