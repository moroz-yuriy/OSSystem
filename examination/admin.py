from django.contrib import admin
from .forms import QuestionForm

from .models import Topic, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]

    form = QuestionForm


class QuestionInline(admin.TabularInline):
    model = Question


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
