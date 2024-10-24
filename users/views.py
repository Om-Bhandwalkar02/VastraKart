from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', context={'form': form})

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<p class='text-red-500 dark:text-red-300 text-xs italic' >Username already exists</p>")
    elif username == '':
        return HttpResponse('')
    else:
        return HttpResponse("<p style='color:#16a34a' class='text-xs italic'>username is available</p>")