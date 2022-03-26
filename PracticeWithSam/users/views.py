from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password


def register(request):
    context = {}
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }
    return render(request, 'users/register.html', context=context)



