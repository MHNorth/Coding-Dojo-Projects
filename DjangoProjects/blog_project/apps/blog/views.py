from django.shortcuts import render, redirect
from django.contrib import messages


def about(request):
        return render(request, "blog/about.html")

def index(request):
    return render(request, "blog/index.html")

def shop(request):
    return render(request, "blog/shop.html")
