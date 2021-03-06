from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class TestModel(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_Submitted = models.DateTimeField(default=datetime.now)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)

    def __str__(self):
        return self.first_name

##model that sets up questions and answers
class QuestionModel(models.Model):
    level = models.CharField(max_length=100,)
    q1 = models.CharField(max_length=200)
    a1 = models.CharField(max_length=100, blank=True)
    q2 = models.CharField(max_length=200)
    a2 = models.CharField(max_length=100, blank=True)
    q3 = models.CharField(max_length=200)
    a3 = models.CharField(max_length=100, blank=True)
    q4 = models.CharField(max_length=200)
    a4 = models.CharField(max_length=100, blank=True)
    timeSetter = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.q1

##model for setup
class UserSetup(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=257)
    email = models.EmailField(max_length=200)
    nameFK = models.ForeignKey(TestModel, on_delete=models.SET_NULL, null=True, blank=True,)

    def __str__(self):
        return self.first_name

##model for vocabulary list options
class VocabularyModel(models.Model):
    w1 = models.CharField(max_length=100,blank=True)
    w2 = models.CharField(max_length=100,blank=True)
    w3 = models.CharField(max_length=100,blank=True)
    w4 = models.CharField(max_length=100,blank=True)



    def __str__(self):
        return self.w1



