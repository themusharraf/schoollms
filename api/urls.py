from django.urls import path
from api.views import LessonView

urlpatterns = [
    path('lessons/', LessonView.as_view(), name='lesson-list-create'),
]
