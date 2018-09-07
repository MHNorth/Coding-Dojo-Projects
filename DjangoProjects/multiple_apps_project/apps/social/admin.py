from django.contrib import admin
from . models import Word, Survey, UploadFile, UploadImage



admin.site.register(Word)
admin.site.register(Survey)
admin.site.register(UploadFile)
admin.site.register(UploadImage)

