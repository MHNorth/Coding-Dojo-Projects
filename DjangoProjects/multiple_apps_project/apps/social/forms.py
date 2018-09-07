from django import forms
from .models import UploadFile, UploadImage


class ImageUploadForm(forms.Form):
    class Meta:
        model = UploadImage
    fields = ('imagefile')


class FileUploadForm(forms.Form):
    class Meta:
        model = UploadFile
    fields = ('documentfile')
   
            



