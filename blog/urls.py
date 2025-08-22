
from django.urls import path
from .views import BlogPostListView
from . import views

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-list'),
    path('<int:pk>/', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('create/', views.BlogPostCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>/', views.BlogPostUpdateView.as_view(), name='blog-update'),
    path('delete/<int:pk>/', views.BlogPostDeleteView.as_view(), name='blog-delete'),
]
