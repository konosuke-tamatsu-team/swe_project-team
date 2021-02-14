from django.contrib import admin

from .models import User, Question,WorkedQuestion


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class Question(admin.ModelAdmin):
    pass

@admin.register(WorkedQuestion)
class WorkedQuestion(admin.ModelAdmin):
    pass