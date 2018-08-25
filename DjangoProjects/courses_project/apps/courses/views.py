from django.shortcuts import render, redirect
from .models import Course



allcourses = Course.objects.all()

def CourseHome(request):
        if request.session:
                context = {
                        'allcourses': allcourses,
                }
        return render(request, 'courses/coursehome.html', context)  

def CourseAdd(request):
        
        addC = Course.objects.addCourse(
                request.POST["course"],
                request.POST["description"],
                )

        return redirect('coursehome')


def RemoveCourseRequest(request):
        return render(request, 'courses/removecourse.html') 

def RemoveCourse(request, id):

        Course.objects.get(id=id).delete()   

        return redirect('coursehome')


