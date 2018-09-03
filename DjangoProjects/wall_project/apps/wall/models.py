from django.db import models


class Post(models.Model):
    post = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post[:50]

class Display(models.Model):
    allUserPost = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __repr__(self):
        return self.allUserPost

