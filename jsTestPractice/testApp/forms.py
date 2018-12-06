from django import forms
from .models import TestModel, UserSetup
from .models import QuestionModel


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['first_name','last_name', ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model= QuestionModel
        fields = ['q1','q2','q3','q4',]


class UserForm(forms.ModelForm):
    class Meta:
        model = UserSetup
        fields = ['first_name','email', 'password',]
        widgets = {
            'password': forms.PasswordInput(),
        }

