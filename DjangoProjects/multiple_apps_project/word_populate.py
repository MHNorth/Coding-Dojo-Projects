import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multiple_apps_project.settings')

import django
django.setup()
import random
from apps.social.models import Word
from faker import Faker
 


fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_word = fakegen.word()
        myword = Word.objects.get_or_create(word=fake_word)[0]
   
    
    
    

if __name__=='__main__':
    print("Populating the database...Please wait")
    populate(150)
    print('Populating Complete')
