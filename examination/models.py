from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Topic(models.Model):
    text = models.CharField(max_length=100, verbose_name='Topic')

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.CharField(max_length=100, verbose_name='Question')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=300, verbose_name='Answer')
    right = models.BooleanField(verbose_name='Right')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
