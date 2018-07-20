from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    return render(request, 'first_app/index.html',)

def about(request):
    return render(request, 'first_app/about.html',)

def blog(request):
    return render(request, 'first_app/blog_post.html',)

def recipe(request):
    return render(request, 'first_app/recipe_post.html',)

def contact(request):
    return render(request, 'first_app/contact.html',)

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")










