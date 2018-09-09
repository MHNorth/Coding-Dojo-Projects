import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_project.settings')

import django
django.setup()

import random
from faker import Faker
from store.models import Customers, AccessRecord

fakegen = Faker()

def populate(N=30):

    for entry in range(N):

        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_address = fakegen.address()  
        fake_city = fakegen.city() 
        fake_state = fakegen.state()
        fake_zip = fakegen.zipcode()
        fake_phone = fakegen.phone_number()
        fake_date = fakegen.date(pattern="%Y-%m-%d", end_datetime=None)

        # Create new Webpage Entry
        cust = Customers.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, address=fake_address, city=fake_city, state=fake_state, zip=fake_zip, created_at=fake_date, updated_at=fake_date)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = AccessRecord.objects.get_or_create(name=fake_fname, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(40)
    print("populating complete!")