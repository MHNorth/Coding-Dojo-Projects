from django.db import models

##---------- Courses Model ----------#

class CourseManager(models.Manager):
    
    def addCourse(self, courseName, description):

        errors = []

        if len(courseName) < 3:
            errors.append("Course name must be 5 characters or longer.")

        if len(description) < 3:
            errors.append("Description must be 15 characters or longer. ")
        
        if len(errors) > 0:
            return {"valid": False, "errors": errors}
        else:
            Course.objects.create(courseName = courseName, description=description)
            return {"valid": False, "errors": errors}


class CourseDesc(models.Model):
    description = models.CharField(max_length=500)
    objects = CourseManager()

    def __repr__(self):
        return "Course Description: {}".format(self.description[0:25])
        

class Course(models.Model):

    courseName = models.CharField(max_length=255)
    courseDescription = models.ForeignKey(CourseDesc, on_delete=models.CASCADE)
    dateAdded = models.DateField(auto_now_add=True)
    objects = CourseManager()

    def __repr__(self):
        return "Course Name: {}".format(self.courseName)






