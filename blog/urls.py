
from django.urls import path
from .views import BlogPostListView
from . import views

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-list'),
    path('/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog-detail'),
]
