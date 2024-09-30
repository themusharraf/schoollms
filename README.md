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

## Ma'lumotlar tuzilmasi:
1. - `Student` modeli: Talabalar haqidagi ma'lumotlarni saqlaydi.
- `full_name`: Talabaning to'liq ismi.
2. - Modul modeli: Har bir modulni ifodalaydi.
- `name`: Modulning nomi.
3. - Lesson modeli: Har bir dars uchun sana, studentlar ro'yxati, modullar ro'yxati va great ma'lumotini saqlaydi.
- `date`: Dars sanasi.
- `name`: Dars nomi.
- `students`: Darsga qatnashayotgan talabalar ro'yxati (ko'plab studentlar bo'lishi mumkin).
- `moduls`: Ushbu darsga tegishli modullar ro'yxati (ko'p modullar bo'lishi mumkin).
- ` great`: Dars natijasi yoki baho (standart holda null yoki bo'sh bo'lishi mumkin).
