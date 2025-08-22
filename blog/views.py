from django.shortcuts import render
from .models import Blog_Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView

# Create your views here.

class BlogPostListView(ListView):
    model = Blog_Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_posts'
    ordering = ['-created_at']
    paginate_by = 5

class BlogPostDetailView(DetailView):
    model = Blog_Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog_post'
    date_field = 'created_at'

class BlogPostCreateView(CreateView):
    model = Blog_Post
    template_name = 'blog/blog_create.html'
    fields = ['title', 'content', 'author']
    
