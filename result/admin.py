from django.contrib import admin
from . import models

@admin.register(models.Result)
class UserAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'number', 'result', 'date')