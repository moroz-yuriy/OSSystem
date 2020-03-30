from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Topic
from .utils import get_next_question


def next_question(view_func):
    def wrap(request, *args, **kwargs):
        question = Question.objects.get(pk=kwargs['question_id'])

        not_answered = get_next_question(request.user, question.topic)
        if len(not_answered) == 0:
            return HttpResponseRedirect(reverse('result', kwargs={'topic_id': question.topic.id}))

        question_id = not_answered.pop()
        kwargs['question_id'] = question_id

        return view_func(request, *args, **kwargs)

    return wrap


def is_finish_topic(view_func):
    def wrap(request, *args, **kwargs):
        topic = Topic.objects.get(pk=kwargs['topic_id'])

        not_answered = get_next_question(request.user, topic)

        if len(not_answered) != 0:
            question_id = not_answered.pop()
            return HttpResponseRedirect(reverse('question', kwargs={'question_id': question_id}))

        return view_func(request, *args, **kwargs)

    return wrap
