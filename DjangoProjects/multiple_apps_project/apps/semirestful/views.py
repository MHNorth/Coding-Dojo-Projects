from django.shortcuts import render, redirect




def UserHome(request):
        return render(request, 'semirestful/usersindex.html')   

def UserEdit(request):
        return render(request, 'semirestful/useredit.html') 

def UserAdd(request):
        return render(request, 'semirestful/useradd.html') 

def UserShow(request):
        return render(request, 'semirestful/usershow.html') 