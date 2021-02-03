from django.contrib import admin

from .models import User, Question


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class Question(admin.ModelAdmin):
    pass