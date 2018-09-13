from django.db import models



class Paste(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    name = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)  #automatically adds current time to the field when object is created
    updated_on = models.DateField(auto_now=True)  #adds the current time to the field each time and object is saved

    def __unicode__(self):
        return 'Name: {} Text: {} Date Created: {}'.format(str(self.name), str(self.text), str(self.created_on))

    #This function glues the create view and detail view together
    @models.permalink   #This decorator tells django to call the url named pastebin_past_detail with the parameter id
    def get_absolute_url(self):  #This will allow the create_object view to call the objects url by default
        return ('pastebin_paste_detail', [self.id])


    

    