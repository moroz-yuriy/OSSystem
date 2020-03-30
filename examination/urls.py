from examination import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('result/<int:topic_id>/', views.result, name='result'),
]
