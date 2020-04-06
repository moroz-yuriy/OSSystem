"""OSSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from examination import views

urlpatterns = [
    path('', views.index, name='index'),
    path('examination/', include('examination.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('login/',
         auth_views.LoginView.as_view(
             redirect_authenticated_user=True,
             success_url=''), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
