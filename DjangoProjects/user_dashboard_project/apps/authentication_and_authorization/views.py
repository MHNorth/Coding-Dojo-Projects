from django.shortcuts import render, redirect
from .models import User, AdminUser
from django.contrib import messages


def index(request):
    if "adminuser_id" in request.session:
        return(redirect("dashadmin"))
    return render(request, 'authentication_and_authorization/register.html')

def register(request):
    results = AdminUser.objects.validate(request.POST)
    if not results[0]:
        for error_message in results[1]:
            messages.add_message(request, messages.ERROR, error_message) 
    return(redirect("dashadmin"))      

def login(request):
    if "user_id" in request.session:
        return(redirect("dashhome"))
    return render(request, 'authentication_and_authorization/login.html')

def log(request):
    results = User.objects.login(request.POST)
    if not results[0]:
        for error_message in results[1]:
            messages.add_message(request, messages.ERROR, error_message)
        return(redirect('/'))
    else:
        request.session["user_id"] = results[1].id
        request.session["full_name"] = results[1].full_name
        return(redirect("dashhome"))


def registercomp(request):
    if "user_id" not in request.session:
        return(redirect("/"))
    return render(request, 'authentication_and_authorization/regcomp.html')


def logout(request):
    request.session.clear()   
    return redirect("/")


