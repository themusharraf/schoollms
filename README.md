# LMS API arxitekturasi

## Modelar tuzilmasi:
```python
from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Modul(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255, null=True, blank=True)
    students = models.ManyToManyField(Student, related_name='lessons')  # students list
    moduls = models.ManyToManyField(Modul, related_name='lessons')  # get post
    great = models.CharField(max_length=5, null=True, blank=True, default=None)  # default null

    def __str__(self):
        return f"Lesson on {self.date}"
```
