from django.forms import ModelForm, forms
from .models import UploadFile, UploadImage, MultipleFiles


class ImageUploadForm(ModelForm):
    class Meta:
        image_model=UploadImage
        fields=['imagefile',]


class FileUploadForm(ModelForm):
    upload_model=UploadFile
    fields=['documentfile',]


class MultipleUploadForm(ModelForm):
    upload_mult=MultipleFiles
    fields= ['documentfile',]



