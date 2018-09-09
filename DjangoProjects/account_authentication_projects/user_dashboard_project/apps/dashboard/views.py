from django.shortcuts import render, redirect




def DashHome(request):
        return render(request, 'dashboard/dashhome.html')   

def DashUser(request):
        return render(request, 'dashboard/userdash.html') 

def DashInfo(request):
        return render(request, 'dashboard/userinfo.html')

def DashAdmin(request):
        return render(request, 'dashboard/dashadmin.html') 

def DashProfile(request):
        return render(request, 'dashboard/editprofile.html') 

def DashEdit(request):
        return render(request, 'dashboard/edituser.html') 

def DashNew(request):
        return render(request, 'dashboard/newuser.html') 





