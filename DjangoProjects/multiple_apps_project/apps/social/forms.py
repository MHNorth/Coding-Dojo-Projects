from django import forms
from .models import UploadFile, UploadImage


class ImageUploadForm(forms.Form):

    thumbfile = forms.ImageField()

    class Meta:
        model = UploadImage
    fields = ('imagefile')



class FileUploadForm(forms.Form):

    thumbimage = forms.FileField()

    class Meta:
        model = UploadFile
    fields = ('documentfile')
            



