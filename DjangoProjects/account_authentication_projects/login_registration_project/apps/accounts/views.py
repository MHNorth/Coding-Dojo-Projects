from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request):
	if "user_id" in request.session:
		return(redirect("dash"))
	return render(request, 'accounts/registration_form.html')

def register(request):

    results = User.objects.validate(request.POST)
    if not results[0]:
        for error_message in results[1]:
            messages.add_message(request, messages.ERROR, error_message) 
    return(redirect("/"))      

def login(request):
    if "user_id" in request.session:
        return(redirect("dash"))
    return render(request, 'accounts/login.html')

def log(request):
    results = User.objects.login(request.POST)
    if not results[0]:
        for error_message in results[1]:
            messages.add_message(request, messages.ERROR, error_message)
        return(redirect('/'))
    else:
        request.session["user_id"] = results[1].id
        request.session["full_name"] = results[1].full_name
        return(redirect("dash"))

def dashboard(request):
    if "user_id" not in request.session:
        return(redirect("/"))

    return render(request, 'accounts/dashboard.html')


def registercomp(request):
    if "user_id" not in request.session:
        return(redirect("/"))
    return render(request, 'accounts/regcomp.html')


def logout(request):
    request.session.clear()   
    return redirect("/")


