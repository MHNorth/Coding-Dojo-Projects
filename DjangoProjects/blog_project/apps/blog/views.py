from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def about(request):
        return render(request, "blog/about.html")

def index(request):
    return render(request, "blog/index.html")

def shop(request):
    return render(request, "blog/shop.html")

def register(request):
    results = User.objects.register(request.POST)
    if results[0]:
        request.session["user_id"] = results[1].id
        return redirect("login")
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect("home")

def login(request):
    results = User.objects.login(request.POST)
    if results[0]:
        request.session["user_id"] = results[1].id
        return redirect("login")
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect("home")

def logout(request):
    request.session.clear()
    return redirect("home")