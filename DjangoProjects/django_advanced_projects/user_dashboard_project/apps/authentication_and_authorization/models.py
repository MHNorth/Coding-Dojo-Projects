from django.db import models
from apps.dashboard.models import Post
from datetime import datetime
from time import  strftime
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]+$')

# Registration and Login Manager
class UserManager(models.Manager):

    #Registration Validation
	def validate(self, form_data):

		errors = []

		# Email
		if len(form_data["email"]) < 1:
			errors.append("Email is required.")
		elif not EMAIL_REGEX.match(form_data["email"]):
			errors.append("Invalid Email")
		else:
			if len(User.objects.filter(email=form_data["email"].lower())) > 0:
				errors.append("Email already in use.")

		# First Name
		if len(form_data["first_name"]) < 1:
			errors.append("Name is required.")
		elif len(form_data["first_name"]) < 2:
			errors.append("Name is too short.")

		# Last Name
		if len(form_data["last_name"]) < 1:
			errors.append("Name is required.")
		elif len(form_data["last_name"]) < 2:
			errors.append("Name is too short.")
		
		# Password
		if len(form_data["password"]) < 1:
			errors.append("Password is required.")
		elif len(form_data["password"]) < 8:
			errors.append("Password must be 8 letters or longer.")

		# Reconfirm Password
		if form_data["password"] != form_data["rec_password"]:
			errors.append("Password and Reconfirmed Password must match.")

		# Final Validation
		if len(errors) > 0:
			return (False, errors)
		else:
			hashed_pw = bcrypt.hashpw(form_data["password"].encode(), bcrypt.gensalt())
			user = User.objects.create(
				email = form_data["email"].lower(),
				first_name = form_data["first_name"],
				last_name = form_data["last_name"],
				password = hashed_pw,
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


# User 
class User(models.Model):
	email = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	user_level = models.CharField(max_length=255)
	userpost = models.ManyToManyField(Post, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	
	def __str__(self):
		return "{} | {} | {}>".format(self.first_name, self.last_name, self.user_level)

# Admin User
class AdminUser(models.Model): 
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	userpost = models.ManyToManyField(Post, blank=True)
	email = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	
	def __str__(self):
		return "{} | {}>".format(self.first_name, self.last_name)   

	