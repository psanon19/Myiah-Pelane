from django.shortcuts import render, get_object_or_404, redirect
from .models import TestModel
from .forms import TestForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def userindex(request):
    form_list = TestModel.objects.filter(username=request.user)
    context = {'form_list': form_list, }
    return render(request, 'testApp/base.html', context)
