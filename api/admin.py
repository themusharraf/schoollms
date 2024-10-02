from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from api.models import GroupClass, GroupLessons, Science, Modul, User, Lesson, LessonSubmission


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    # Customizing list display
    list_display = ('username', 'email', 'full_name', 'is_teacher', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('is_teacher', 'is_staff', 'is_superuser', 'is_active', 'groups')

    # Fields to be shown in User change form (admin page to edit user)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_teacher', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to be shown in User creation form (admin page to add a user)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'password1', 'password2'),
        }),
    )

    # Defining ordering in the list display
    ordering = ('username',)

    # Fields displayed in the user detail view (after clicking on a user)
    readonly_fields = ('last_login', 'date_joined')


@admin.register(GroupClass)
class GroupClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')  # Display group name and timestamps
    search_fields = ('name',)  # Enable search by group name
    filter_horizontal = ('students',)  # For ManyToMany fields


@admin.register(GroupLessons)
class GroupLessonsAdmin(admin.ModelAdmin):
    list_display = ('group', 'science', 'teacher', 'created', 'updated')
    search_fields = ('group__name', 'science__name', 'teacher__full_name')  # Enable search by related fields
    list_filter = ('science', 'teacher')


@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)


@admin.register(Modul)
class ModulAdmin(admin.ModelAdmin):
    list_display = ('name', 'science', 'created', 'updated')
    search_fields = ('name', 'science__name')
    list_filter = ('science',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'modul', 'created', 'updated')
    search_fields = ('name', 'modul__name')
    list_filter = ('modul',)
    filter_horizontal = ('students',)


@admin.register(LessonSubmission)
class LessonSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'grade', 'created', 'updated')
    search_fields = ('student__full_name', 'lesson__name')
    list_filter = ('grade',)
