from django.shortcuts import render, redirect
from .models import Course, CourseDesc
from django.contrib import messages



allcourses = Course.objects.all()

def CourseHome(request):
        if request.session:
                context = {
                        'allcourses': allcourses,
                }
        return render(request, 'courses/coursehome.html', context)  



def CourseAdd(request):
        if request.POST:
                Course.objects.addCourse(
                request.POST["course"],
                request.POST["description"],
                )

        return redirect('coursehome')



def RemoveCourseRequest(request):
        context = {
                'course': Course.objects.get(id=id)
        }
        return render(request, 'courses/removecourse.html', context) 


def RemoveCourse(request, course_id):
        
        Course.objects.get(id=id).delete()   

        return redirect('coursehome')


