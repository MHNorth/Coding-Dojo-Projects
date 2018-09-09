import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multiple_apps_project.settings')

import django
django.setup()
import random
from apps.accounts.models import User
from faker import Faker
 


fakegen = Faker()


def populateSocial(N=5):

    for entry in range(N):
        fake_name = fakegen.name()    
        fake_alias = fakegen.first_name()       
        fake_email = fakegen.email()
        fake_pw = fakegen.password(length=8, special_chars=False, digits=True, upper_case=False, lower_case=True)    
        fake_birthdate = fakegen.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=115)

        socialUser = User.objects.get_or_create(name=fake_name, alias=fake_alias, email=fake_email, password=fake_pw, birthdate=fake_birthdate)[0]
    



if __name__=='__main__':
    print("Populating the database...Please wait")
    populateSocial(20)
    print('Populating Complete')
