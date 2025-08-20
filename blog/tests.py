from django.test import TestCase
from django.urls import reverse
from .models import Blog_Post
from django.contrib.auth import get_user_model


# Create your tests here.
class BlogPostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post = Blog_Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )

    def test_blog_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post.')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_blog_post_list_view(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_blog_post_detail_view(self):
        response = self.client.get(reverse('blog-detail', args=[self.post.id]))
        No_response = self.client.get(reverse('blog-detail', args=['1000']))
        self.assertEqual(No_response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test post.')
        self.assertTemplateUsed(response, 'blog/blog_detail.html') 

