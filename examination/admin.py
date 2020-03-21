from django.contrib import admin
from .models import Topic, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]


class QuestionInline(admin.TabularInline):
    model = Question


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
