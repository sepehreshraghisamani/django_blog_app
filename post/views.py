from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# def list_post(request):
#     post = Post.objects.all()
#     return render(request, 'post/list.html', {'post': post})

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'
    context_object_name = 'post'  # This will be used in the template to refer to the list of posts

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')  # Order by creation date, newest first   
