from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {"form": form}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('TODO'))
    else:
        return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            return response
        else:
            messages.info(
                request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('TODO'))
    else:
        return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('TODO'))
    return response