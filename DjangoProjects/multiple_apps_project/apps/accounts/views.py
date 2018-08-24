from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages




def register(request):
    if request.method == "POST":
        results = User.objects.register(request.POST)
        print(request.POST)
        if results[0]:
            request.session["user_id"] = results[1].id
            request.session["full_name"] = results[1].full_name
            request.session["alias"] = results[1].alias
            return redirect("/friends/{}".format(request.session["user_id"]))
        else:
            for error in results[1]:
                messages.add_message(request, messages.ERROR, error)
    return render(request, 'accounts/registration_form.html')
    

def login(request):
    if request.method == "POST":
        print(request.POST)
        results = User.objects.login(request.POST)

        if results[0]:
            request.session["user_id"] = results[1].id
            request.session["full_name"] = results[1].full_name
            request.session["alias"] = results[1].alias
            return redirect("/friends/{}".format(request.session["user_id"]))
        else:
            for error in results[1]:
                messages.add_message(request, messages.ERROR, error)
            return redirect("login")
    return render(request, 'accounts/login.html')


def registercomp(request):
    if "user_id" not in request.session:
        messages.add_message(request, messages.ERROR, "You need to login first")
        return(redirect("login"))
    return render(request, 'accounts/regcomp.html')


def logout(request):
    request.session.clear()   
    return redirect('homepage')


