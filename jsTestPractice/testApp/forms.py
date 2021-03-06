from django import forms
from .models import TestModel, UserSetup , VocabularyModel
from .models import QuestionModel



class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['first_name','last_name', ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model= QuestionModel
        fields = ['a1','a2','a3','a4','timeSetter',]


class UserForm(forms.ModelForm):
    class Meta:
        model = UserSetup
        fields = ['first_name','email', 'password',]
        widgets = {
            'password': forms.PasswordInput(),
        }

class VocabularyForm(forms.ModelForm):
    class Meta:
        model = VocabularyModel
        fields = ['w1','w2','w3','w4']

