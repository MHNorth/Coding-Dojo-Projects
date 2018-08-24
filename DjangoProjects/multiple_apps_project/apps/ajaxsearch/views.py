from django.shortcuts import render, redirect


def Search(request):
        return render(request, 'ajaxsearch/index.html') 
