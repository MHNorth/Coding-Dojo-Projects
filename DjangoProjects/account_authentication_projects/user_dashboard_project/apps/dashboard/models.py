from django.db import models



# Post
class Post(models.Model):
	post = models.TextField(max_length=500)

	def __str__(self):
		return "User: {}, {} | Post: {}>".format(self.last_name, self.first_name, self.post)
