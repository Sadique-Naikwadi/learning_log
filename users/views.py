from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_user(request):

    if request.method == 'POST':

        form  = LoginForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('learning_logs:topics')
            else:
                 return redirect('learning_logs:index')


        else:

            form.errors

    else:

        form = LoginForm()

    context = {'form': form, 'errors': form.errors}
    return render(request, 'users/login.html', context)


def register(request):

    if request.method != 'POST':

        form = UserCreationForm()

    else:

        form = UserCreationForm(request.POST)

        if form.is_valid():

            new_user = form.save()
            login(request, new_user)
            
            return redirect('learning_logs:topics')

        
    context = {'form': form}

    return render(request, 'registration/register.html', context)
