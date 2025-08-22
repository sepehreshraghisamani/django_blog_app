from django.shortcuts import render
from .models import Blog_Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

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

class BlogPostUpdateView(UpdateView):
    model = Blog_Post
    template_name = 'blog/blog_update.html'
    fields = ['title', 'content']
    context_object_name = 'blog_post'
    
    def get_success_url(self):
        return self.object.get_absolute_url()  # Assuming you have a get_absolute_url method in your model

class BlogPostDeleteView(DeleteView):
    model = Blog_Post
    template_name = 'blog/blog_delete.html'
    context_object_name = 'blog_post'
    success_url = reverse_lazy('blog-list')
    
