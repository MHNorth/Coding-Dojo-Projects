from django.forms import ModelForm  #ModelForm includes a save method (just like a Models save method) which saves the model data to the database.
from .models import Post, Comment


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text',)



class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)