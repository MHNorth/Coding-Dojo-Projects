from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.dates import MonthArchiveView, WeekArchiveView
from django.shortcuts import redirect, render_to_response, get_object_or_404, render

from .models import Post
from .forms import PostForm, CommentForm

"""
Views needed:
Admin should be able to login
Add/Edit a post - restricted to admin
View a blog post
Comment on a blog post
"""


def Home(request):
        return render(request, 'blog/index.html') 

def Fashion(request):
        return render(request, 'blog/fashion.html')  

def Model(request):
        return render(request, 'blog/model.html')  

def Travel(request):
        return render(request, 'blog/travel.html')  

def Contact(request):
        return render(request, 'blog/contact.html')  

def About(request):
        return render(request, 'blog/about.html')  

def BlogPage(request):
        return render(request, 'blog/blog.html')  

def PostDetail(request):
        return render(request, 'blog/post_detail.html')  

@user_passes_test(lambda u: u.is_superuser)  #The user_passes_test decorator tests whether the user is admin or not. If not, it will redirect the user to login page.
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)  #commit=False on a form save gives us the temporary Model object so that we can modify it and save permanently. Here, we have used it to autofill the author of Post and post of Comment
        post.author = request.user
        post.save()
        return redirect(post)
    return render(request, 'blog/add_post.html',{ 'form': form })

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    #  Here is where we store the commenter’s details in the session so that he/she does not have to fill them again
        request.session["name"] = comment.name
        request.session["email"] = comment.email
        request.session["website"] = comment.website
        return redirect(request.path)
    form.initial['name'] = request.session.get('name')  #the form.initial attribute is a dict that holds initial data of the form. A session lasts until the user logs out or clears the cookies (e.g. by closing the browser). django identifies the session using sessionid cookie.
    form.initial['email'] = request.session.get('email')
    form.initial['website'] = request.session.get('website')
    return render(request, 'blog/view_post.html',{'post': post,'form': form,})

#PostMonthArchiveView generic class based views outputs to post_archive_month.html and PostWeekArchiveView to post_archive_week.html
class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "created_on"
    allow_future = True

class PostWeekArchiveView(WeekArchiveView):
    queryset = Post.objects.all()
    date_field = "created_on"
    week_format = "%W"
    allow_future = True

def New(request):
        return render(request, 'blog/post_home.html')  

def Edit(request):
        return render(request, 'blog/post_home.html')  

def Drafts(request):
        return render(request, 'blog/post_draft.html')  

def PostRemove(request):
        return render(request, 'blog/post_confirm_delete.html')

def Publish(request):
        return render(request, 'blog/post_home.html')  

def Comment(request):
        return render(request, 'blog/post_home.html')  

def Approve(request):
        return render(request, 'blog/post_home.html')  

def CommentRemove(request):
        return render(request, 'blog/post_home.html')    


# class PostListView(ListView):
#     model = Post

#     def get_queryset(self):
#         return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# class PostDetailView(DetailView):
#     model = Post


# class CreatePostView(LoginRequiredMixin,CreateView):
#     login_url = '/login/'
#     redirect_field_name = 'blog/post_detail.html'

#     form_class = PostForm

#     model = Post


# class PostUpdateView(LoginRequiredMixin,UpdateView):
#     login_url = '/login/'
#     redirect_field_name = 'blog/post_detail.html'

#     form_class = PostForm

#     model = Post


# class DraftListView(LoginRequiredMixin,ListView):
#     login_url = '/login/'
#     redirect_field_name = 'blog/post_draft_list.html'

#     model = Post

#     def get_queryset(self):
#         return Post.objects.filter(published_date__isnull=True).order_by('created_date')


# class PostDeleteView(LoginRequiredMixin,DeleteView):
#     model = Post
#     success_url = reverse_lazy('post_list')

# #######################################
# ## Functions that require a pk match ##
# #######################################

# @login_required
# def post_publish(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.publish()
#     return redirect('post_detail', pk=pk)

# @login_required
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/comment_form.html', {'form': form})


# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post_detail', pk=comment.post.pk)


# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post_pk = comment.post.pk
#     comment.delete()
#     return redirect('post_detail', pk=post_pk)
