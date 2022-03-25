from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserCreationForm


def register(request):
    context = {}
    form = UserCreationForm(request,)
    context = {
        'form': form
    }
    return render(request,'users/register.html',context=context)
