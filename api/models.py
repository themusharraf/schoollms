from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseDate(models.Model):
    """created va updated date ma'lumotlarini saqlash uchun abstract model"""  # noqa
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class GroupClass(BaseDate):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField('User')


class GroupLessons(BaseDate):
    group = models.ForeignKey(GroupClass, related_name='lessons', on_delete=models.CASCADE)
    science = models.ForeignKey('Science', related_name='groups', on_delete=models.PROTECT)
    teacher = models.ForeignKey('User', related_name='groups_class', on_delete=models.PROTECT)


class Science(BaseDate):
    """Fanlar uchun model"""  # noqa
    name = models.CharField(max_length=255)


class Modul(BaseDate):
    """Fanlarning modullarini saqlash uchun model"""  # noqa
    name = models.CharField(max_length=255)
    science = models.ForeignKey(Science, related_name='moduls', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Django'ning o'zida parolni boshqarish # noqa
    is_teacher = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class Lesson(BaseDate):
    """Darslar uchun model"""  # noqa

    modul = models.ForeignKey(Modul, related_name='lessons', on_delete=models.PROTECT)  # get post
    name = models.CharField(max_length=255, null=True, blank=True)
    lesson_text = models.TextField()

    students = models.ManyToManyField(User, related_name='lessons')  # students list

    def __str__(self):
        return f"Lesson on {self.date}"


class LessonSubmission(BaseDate):
    """Darslarda o'quvchilarni baholash uchun model"""  # noqa

    student = models.ForeignKey(User, related_name='grades',
                                on_delete=models.PROTECT)  # 1 ta student uchun 1 ta baho # noqa
    grade = models.CharField(max_length=5, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, related_name='grades', on_delete=models.PROTECT)  # get post

    def __str__(self):
        return f"{self.lesson.id} > {self.student.full_name} > {self.grade}"
