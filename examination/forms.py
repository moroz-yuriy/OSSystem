from django import forms

from .models import Answer, Question


class AnswerForm(forms.Form):
    class Meta:
        model = Answer

    def __init__(self, question, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(
            Answer.objects.filter(question=question),
            widget=forms.RadioSelect,
            empty_label=None
        )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        answers_count = int(self.data.get('answer_set-TOTAL_FORMS', 0))
        count_right = 0
        count = 0
        for i in range(0, answers_count):
            if self.data.get('answer_set-{0}-text'.format(i), '') != '':
                count = count + 1
                if self.data.get('answer_set-{0}-right'.format(i), '') == 'on':
                    count_right = count_right + 1

        if count < 2:
            raise forms.ValidationError('There must be at least two answers')

        if count == count_right:
            raise forms.ValidationError('All answers may not be correct!')

        if count_right == 0:
            raise forms.ValidationError('At least one answer must be correct')
