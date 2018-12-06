from django.shortcuts import render, get_object_or_404, redirect
from .models import TestModel, QuestionModel
from .forms import TestForm, QuestionForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required()
def userindex(request):
    form_list = TestModel.objects.filter(username=request.user)
    context = {'form_list': form_list, }
    return render(request, 'testApp/index.html', context)



def questions(request):
    question_list = QuestionModel.objects.all()
    context = {'question_list': question_list,}
    return render(request,'testApp/start_test.html', context)

def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
         return render(request, 'testApp/index.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'testApp/index.html', {'form': form})
