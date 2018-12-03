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
