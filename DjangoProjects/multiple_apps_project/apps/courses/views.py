from django.shortcuts import render, redirect
from time import localtime, strftime
# from .models import Courses





def CourseHome(request):
        return render(request, 'courses/coursehome.html')  

def CourseAdd(request):
        date_now = strftime("%B %d, %Y %H:%M %p", localtime())
        if request.method == "POST":
                request.session["course"] = request.POST["course"]
                request.session["description"] = request.POST["description"]
                request.session["date"] = date_now

        return redirect('coursehome')

def RemoveCourseRequest(request):
        request.session
        return render(request, 'courses/removecourse.html') 

def RemoveCourse(request):
        request.session.clear()
        return redirect('coursehome')


