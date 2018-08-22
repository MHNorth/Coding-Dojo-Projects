from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages




def register(request, *args, **kwargs):
    # results = User.objects.register(request.POST)
    # if not results[0]:
    #     for error_message in results[1]:
    #         messages.add_message(request, messages.ERROR, error_message)
    #     return(redirect("register"))
    return render(request, 'accounts/registration_form.html')
    

def login(request, *args, **kwargs):
    # results = User.objects.login(request.POST)
    # if not results[0]:
    #     for error_message in results[1]:
    #         messages.add_message(request, messages.ERROR, error_message)
    #     return(redirect("register"))
    # else:
    #     request.session["user_id"] = results[1].id
    #     request.session["full_name"] = results[1].full_name
    #     return(redirect("friends"))
    return render(request, 'accounts/login.html')


def registercomp(request, *args, **kwargs):
    # if "user_id" in request.session:
    #     return(redirect("rcomplete"))
    return render(request, 'accounts/regcomp.html')


def logout(request, *args, **kwargs):
    # request.session.clear()   
    return redirect("register")


