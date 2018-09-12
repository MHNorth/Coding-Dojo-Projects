from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy


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
