from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "books/index.html")
