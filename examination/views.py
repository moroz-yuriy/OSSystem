from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import QuestionsForm
from .models import Topic, Question, Result


def index(request):
    topics = Topic.objects.all()
    return render(request, 'index.html', {'topics': topics})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='/login')
def topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    question = topic.question_set.first()
    return render(request, 'examination/topic.html', {'topic': topic, 'question': question})


@login_required(login_url='/login')
def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

        if request.method == 'POST':
            form = QuestionsForm(question, request.POST)
            if form.is_valid():
                Result.objects.create(user=request.user, )
                return HttpResponseRedirect(reverse('question', kwargs={'question_id': question.id + 1}))

        form = QuestionsForm(question)
        return render(request, 'examination/question.html', {'question': question, 'form': form})
    except ObjectDoesNotExist:
        raise Http404
