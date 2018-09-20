from django.db import models
from django.core import validators



##----------- Word Generator Model ------------##

class Word(models.Model):

    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word

##----------- Survey Model -----------##

class Survey(models.Model):

    fullName = models.CharField(max_length=50)

    dojo_locations = (
        ('Tyson\'s Corner', "Tyson's Corner"),
        ('Seattle', 'Seattle'),
        ('San Jose', 'San Jose'),
    )

    favoriteLanguage = (
        ('Python', 'Python'),
        ('Javascript', 'Javascript'),
        ('Java', 'Java'),
    )
    yourDojo = models.CharField(
        max_length=50,
        choices = dojo_locations,
        default = "Tyson's Corner"
    )
    yourLanguage = models.CharField(
        max_length = 50,
        choices = favoriteLanguage,
        default = 'Python'
    )

    comment = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Name: {}, Dojo: {}, Lang: {}".format(self.fullName, self.yourDojo, self.yourLanguage)


##----------- Upload Files and Images Model -----------##


class UploadFile(models.Model):
    documentfile = models.FileField(upload_to='documents/%m-%d-%y/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    def __obj__(self):
        return '%s' % self.documentfile


class UploadImage(models.Model):      
    imagefile = models.ImageField(upload_to='pictures/%m-%d-%y/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __obj__(self):
        return '%s' % self.imagefile

    







    


    