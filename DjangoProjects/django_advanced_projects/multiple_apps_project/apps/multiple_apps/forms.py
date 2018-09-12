from django import forms
from .models import UploadFile, UploadImage


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=UploadImage
        fields=('imagefile',)
        widgets = {
        "title": forms.TextInput(
                attrs={
                    "required": "True",
                    "autofocus": "True",
                }
            ),
        "imagefile": forms.FileInput(attrs={'multiple': True}),
        }



class FileUploadForm(forms.ModelForm):
    docfile = forms.FileField(
        label='Select a file',
    )


            



