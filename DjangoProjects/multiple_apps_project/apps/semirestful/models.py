from django.db import models


##---------- Semi-Restful Model -----------#

class RestUser(models.Model):

    fullName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullName
