from django.contrib import admin
from .models import Course, Question

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'introduce', 'create_time')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'title', 'type', 'score', 'create_time')