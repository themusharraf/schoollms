# LMS API arxitekturasi

## Modelar tuzilmasi:
```python
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

```

## Ma'lumotlar tuzilmasi:
1. Student modeli: Talabalar haqidagi ma'lumotlarni saqlaydi.
- `full_name`: Talabaning to'liq ismi.
2. Modul modeli: Har bir modulni ifodalaydi.
- `name`: Modulning nomi.
3. Lesson modeli: Har bir dars uchun sana, studentlar ro'yxati, modullar ro'yxati va great ma'lumotini saqlaydi.
- `date`: Dars sanasi.
- `name`: Dars nomi.
- `students`: Darsga qatnashayotgan talabalar ro'yxati (ko'plab studentlar bo'lishi mumkin).
- `moduls`: Ushbu darsga tegishli modullar ro'yxati (ko'p modullar bo'lishi mumkin).
- `great`: Dars natijasi yoki baho (standart holda null yoki bo'sh bo'lishi mumkin).

## API serializers.py:
API orqali ma'lumotlarni serializerlar orqali ko'rsatish uchun `serializers.py` faylini yaratishingiz mumkin:
```python
from rest_framework import serializers
from .models import Student, Modul, Lesson

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name']

class ModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modul
        fields = ['id', 'name']

class LessonSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    moduls = ModulSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['date', 'name', 'students', 'moduls', 'great']
```
