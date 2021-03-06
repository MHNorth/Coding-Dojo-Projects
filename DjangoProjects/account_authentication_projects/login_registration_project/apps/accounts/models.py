from django.db import models
from datetime import datetime
from time import  strftime
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]+$')

# Registration and Login Manager
class RegManager(models.Manager):

    #Registration Validation
	def validate(self, form_data):

		errors = []

		# Name
		if len(form_data["full_name"]) < 1:
			errors.append("Name is required.")
		elif len(form_data["full_name"]) < 2:
			errors.append("Full Name is too short.")

		# Alias
		if len(form_data["alias"]) < 1:
			errors.append("Alias is required.")
		elif len(form_data["alias"]) < 2:
			errors.append("Alias is too short.")

		# Email
		if len(form_data["email"]) < 1:
			errors.append("Email is required.")
		elif not EMAIL_REGEX.match(form_data["email"]):
			errors.append("Invalid Email")
		else:
			if len(User.objects.filter(email=form_data["email"].lower())) > 0:
				errors.append("Email already in use.")
		
		# Password
		if len(form_data["password"]) < 1:
			errors.append("Password is required.")
		elif len(form_data["password"]) < 8:
			errors.append("Password must be 8 letters or longer.")

		# Reconfirm Password
		if form_data["password"] != form_data["rec_password"]:
			errors.append("Password and Reconfirmed Password must match.")

		# Date
		if len(form_data["b-date"]) < 1:
			errors.append("Birthdate is required.")
		else:
			d = datetime.datetime.strptime(form_data["b-date"], "%Y-%M-%d").date()
			datenow = datetime.strptime("%Y-%M-%d")			
			if d > datenow:
				errors.append("The date must be in the past!")
		if len(errors) > 0:
			return (False, errors)
		else:
			day = User.objects.create(date=d)
			return (True, day)


		# Final Validation
		if len(errors) > 0:
			return (False, errors)
		else:
			hashed_pw = bcrypt.hashpw(form_data["password"].encode(), bcrypt.gensalt())
			user = User.objects.create(
				full_name = form_data["full_name"],
				alias = form_data["alias"],
				email = form_data["email"].lower(),
				password = hashed_pw,
				birthdate = form_data["b-date"],
			)
			return (True, user)

    # Login Validation
	def login(self, form_data):

		errors = []

		# Email
		if len(form_data["email"]) < 1:
			errors.append("Email is required.")
		elif not EMAIL_REGEX.match(form_data["email"]):
			errors.append("Invalid Email.")
		else:
			if len(User.objects.filter(email=form_data["email"].lower())) < 1:
				errors.append("Login Failed.")

		if len(form_data["password"]) < 1:
			errors.append("Password is required.")
		elif len(form_data["password"]) < 8:
			errors.append("Password must be 8 letters or longer.")

		if len(errors) > 0:
			return (False, errors)

		user = User.objects.filter(email=form_data["email"].lower())[0]
		hashed_pw = user.password.split("'")[1]

		if bcrypt.checkpw(form_data["password"].encode(), hashed_pw.encode()):
			return (True, user)
		else:
			errors.append("Invalid Login.")
			return (False, errors)

# User Class
class User(models.Model):  
    full_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()

    def __str__(self):
        return "{} | {} | {}>".format(self.full_name, self.alias, self.birthdate)

    