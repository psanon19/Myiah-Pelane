from django import forms
from .models import TestModel


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['first_name','last_name', ]
