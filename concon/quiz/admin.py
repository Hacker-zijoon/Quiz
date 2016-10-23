from django.contrib import admin

from .models import Quiz
from .models import Question
from .models import Answer
from .models import UserScore
from .models import Result


# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated']
    list_display_links = ['id', 'title']
    search_fields = ['title']

admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['quiz', 'sequence']

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['quiz', 'sequence']

admin.site.register(Answer)
admin.site.register(UserScore)
admin.site.register(Result)
