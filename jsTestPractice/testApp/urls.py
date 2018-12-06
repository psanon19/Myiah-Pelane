from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.userindex, name='userindex'),
    path('user/', views.questions, name='question'),
    path('start/', views.get_form, name = 'theform')
    ]
