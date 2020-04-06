from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from .decorators import is_finish_topic, next_question
from .forms import AnswerForm
from .models import Topic, Question, Result
from .utils import get_result, get_next_question


def index(request):
    topics = Topic.objects.all()
    return render(request, 'index.html', {'topics': topics})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            return redirect('registration/login_error.html', message='Login error, try')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup_view(request):
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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='/login')
@is_finish_topic
def topic_view(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    question = topic.question_set.first()
    return render(request, 'examination/topic.html', {'topic': topic, 'question': question})


@login_required(login_url='/login')
@next_question
def question_view(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

        if request.method == 'POST':
            form = AnswerForm(question, request.POST)
            if form.is_valid():
                answer = form.cleaned_data['answer']
                Result.objects.create(user=request.user, topic=question.topic, question=question, answer=answer)
                return HttpResponseRedirect(reverse('question', kwargs={'question_id': question.id}))

        form = AnswerForm(question)
        return render(request, 'examination/question.html', {'question': question, 'form': form})
    except ObjectDoesNotExist:
        raise Http404


@login_required(login_url='/login')
@is_finish_topic
def result_view(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
        user_result = get_result(Result.objects.filter(user=request.user, topic=topic).all())
        return render(request, 'examination/result.html', {'user_result': user_result})
    except ObjectDoesNotExist:
        raise Http404
