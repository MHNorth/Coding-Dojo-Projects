from django.db import models

class LibraryItem(models.Model):

    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject

