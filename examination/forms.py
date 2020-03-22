from django import forms

from .models import Answer


class QuestionsForm(forms.Form):
    class Meta:
        model = Answer

    def __init__(self, question, *args, **kwargs):
        super(QuestionsForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(
            Answer.objects.filter(question=question),
            widget=forms.RadioSelect,
            empty_label=None
        )
