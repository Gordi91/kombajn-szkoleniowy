from django.contrib import admin
from .models import Exam, Exercise, ExerciseStudent
# Register your models here.


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass


@admin.register(ExerciseStudent)
class ExerciseStudentAdmin(admin.ModelAdmin):
    pass
