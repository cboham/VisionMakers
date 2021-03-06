from django.shortcuts import render
from .forms import UserForm, UserProfileForm
from django.urls import reverse,  reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'users/index.html')

def create_profile(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'users/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered':registered
    })

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:home"))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("users:home"))

            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {}".format(username))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request, 'users/login.html', {})
