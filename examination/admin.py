from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import forms
from django.contrib import messages

from .models import Topic, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]

    def save_related(self, request, form, formsets, change):
        try:
            data = formsets[0].cleaned_data
            count_right = 0
            count = 0
            for answer in data:
                if len(answer) > 0:
                    count = count + 1
                    if answer['right']:
                        count_right = count_right + 1

            if count < 2:
                raise forms.ValidationError('There must be at least two answers')

            if count == count_right:
                raise forms.ValidationError('All answers may not be correct!')

            if count_right == 0:
                raise forms.ValidationError('At least one answer must be correct')

            super(QuestionAdmin, self).save_related(request, form, formsets, change)
        except ValidationError as e:
            messages.error(request, e.message);



class QuestionInline(admin.TabularInline):
    model = Question


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
