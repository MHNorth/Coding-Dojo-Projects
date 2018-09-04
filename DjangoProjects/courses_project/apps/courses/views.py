from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages




def CourseHome(request):
        return render(request, 'courses/coursehome.html')  


def CourseAdd(request):
        if request.session == "POST":
                allcourses= Course.objects.all()
                results = Course.objects.ValidCourse(request.POST)
                if not results[0]:
                        for error_message in results[1]:
                                messages.add_message(request, messages.ERROR,error_message)
                        return redirect('coursehome')
                else:
                        return redirect('coursehome')


def RemoveCourseRequest(request):
        
        return render(request, 'courses/removecourse.html') 



def RemoveCourse(request, course_id):
        
        Course.objects.get(id=course_id).delete()   

        return redirect('coursehome')


