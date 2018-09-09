from django.shortcuts import render, redirect
from .models import Post




def WallHome(request):
        allposts = Post.objects.all()
        context = {
                'allposts': allposts,
        }
        return render(request, 'wall/wallhome.html', context)   




