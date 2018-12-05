from django import forms
from .models import TestModel
from .models import QuestionModel


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['first_name','last_name', ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model= QuestionModel
        fields = ['q1','q2','q3','q4',]
