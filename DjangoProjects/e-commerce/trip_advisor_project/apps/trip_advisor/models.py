from django.db import models
import re, bcrypt
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def register(self, form_data):
        # print("inside of your models!!!", form_data)
        errors = []

        if len(form_data["first_name"]) < 1:
            errors.append("First name is required")
        elif len(form_data["first_name"]) < 2:
            errors.append("First name must be 2 letters or longer")
        
        if len(form_data["last_name"]) < 1:
            errors.append("Last name is required")
        elif len(form_data["last_name"]) < 2:
            errors.append("Last name must be 2 letters or longer")

        if len(form_data["email"]) < 1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(form_data["email"]):
            errors.append("Invalid Email")
        else:
            if len(User.objects.filter(email=form_data["email"].lower())) > 0:
                errors.append("Email already in use")

        if len(form_data["password"]) < 1:
            errors.append("Password is required")
        elif len(form_data["password"]) < 8:
            errors.append("Password must be 8 letters or longer")

        if len(form_data["confirm"]) < 1:
            errors.append("Confirm Password is required")
        elif form_data["password"] != form_data["confirm"]:
            errors.append("Confirm Password must match Password")

        if len(errors) == 0:
            hashed_pw = bcrypt.hashpw(form_data["password"].encode(), bcrypt.gensalt())
            print(str(hashed_pw))
            user = User.objects.create(
                first_name = form_data["first_name"],
                last_name = form_data["last_name"],
                email = form_data["email"].lower(),
                password = hashed_pw
            )
            return (True, user)
        else:
            return (False, errors)

    def login(self, form_data):

        errors = []

        if len(form_data["email"]) < 1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(form_data["email"]):
            errors.append("Invalid Email")
        else:
            if len(User.objects.filter(email=form_data["email"].lower())) < 1:
                errors.append("Unknown email {}".format(form_data["email"]))

        if len(form_data["password"]) < 1:
            errors.append("Password is required")
        elif len(form_data["password"]) < 8:
            errors.append("Password must be 8 letters or longer")


        # print(hashed_pw)

        if len(errors) > 0:
            return (False, errors)

        user = User.objects.filter(email=form_data["email"].lower())[0]
        hashed_pw = user.password.split("'")[1]

        if bcrypt.checkpw(form_data["password"].encode(), hashed_pw.encode()):
            return (True, user)
        else:
            errors.append("Incorrect Password")
            return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager(

    )

class TripManager(models.Manager):
    def add(self, form_data, user_id):
        # print(form_data)

        errors = []
        if len(form_data['destination']) < 1:
            errors.append("destination is required")
        elif len(form_data['destination']) < 6:
            errors.append("destination must be 6 characters or more")
        
        if len(form_data['description']) < 1:
            errors.append("description is required")
        elif len(form_data['description']) < 6:
            errors.append("description must be 6 characters or more")
# date validation

        if len(form_data["startdate"]) < 1:
            errors.append("You must enter a date!")
        else:
            d = datetime.strptime(form_data["startdate"], "%Y-%m-%d")
            if d < datetime.now():
                errors.append("The date must be in the Future!")
        
        if len(form_data["enddate"]) < 1:
            errors.append("You must enter a date!")
        else:
            end = datetime.strptime(form_data["enddate"], "%Y-%m-%d")
            if end < d:
                errors.append("The enddate must be later than startdate")

        if len(errors) > 0:
            return (False, errors)

        else:
            trip = Trip.objects.create(
                destination = form_data['destination'],
                description = form_data['description'],
                startdate = form_data['startdate'],
                enddate = form_data['enddate'],
                seller_id = user_id,
            )
            return (True, trip)

    

    #     Jointrip.objects.create(
    #         trip_id = trip_id,
    #         user_id = buyer_id
    #     )
    #     return True

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    seller = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    # joined = models.BooleanField() ---??? come back to this
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TripManager()

class JointripManager(models.Manager):
    def join(self, trip_id, buyer_id):
        trip = Trip.objects.get(id=trip_id)
        joined_trips = Jointrip.objects.filter(trip_id=trip_id).filter(user_id=buyer_id)
        if len(joined_trips) == 0:
            Jointrip.objects.create(trip_id = trip_id, user_id = buyer_id)


class Jointrip(models.Model):
    trip = models.ForeignKey(Trip, related_name="jointrip", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="jointrip", on_delete=models.CASCADE)

    objects = JointripManager()