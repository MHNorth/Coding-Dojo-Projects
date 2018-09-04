from django.db import models


##---------- Courses Model ----------#

class CourseManager(models.Manager):
    
    def ValidCourse(self, form_data):
        errors = []

        if len(form_data["course"]) < 1:
            errors.append("Course name is required.")
        elif len(form_data["course"]) < 5:
            errors.append("Course name must be 5 characters or longer.")

        if len(form_data["description"]) < 1:
            errors.append("Description is required.")
        elif len(form_data["description"]) < 15:
            errors.append("Description must be 15 characters or longer. ")
        
        if len(errors) > 0:
            return (False, errors)

        addCourse = Course.objects.create(
            courseName = form_data["course"], 
            courseDetail= form_data["description"],
            )

        return (True, addCourse)
        

class Course(models.Model):

    courseName = models.CharField(max_length=255)
    courseDetail = models.CharField(max_length=500)
    dateAdded = models.DateField(auto_now_add=True)
    objects = CourseManager()

    def __str__(self):
        return "Course Name: {} | Course Description: {}".format(self.courseName, self.description[0:25])






