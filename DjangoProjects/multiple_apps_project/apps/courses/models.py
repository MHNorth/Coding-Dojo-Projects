from django.db import models

##---------- Courses Model ----------#

class Courses(models.Model):

    courseName = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    dateAdded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courseName
