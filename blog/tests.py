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
    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), f'/blog/{self.post.id}/')
    
    def test_create_blog_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('blog-create'), {
            'title': 'New Post',
            'content': 'This is a new post.',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog_Post.objects.last().title, 'New Post')
        self.assertEqual(Blog_Post.objects.last().content, 'This is a new post.')
    
    def test_update_blog_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('blog-update', args=[self.post.id]), {
            'title': 'Updated Post',
            'content': 'This is an updated post.',
            'author': self.user.id
        })
        self.post.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.title, 'Updated Post')
        self.assertEqual(self.post.content, 'This is an updated post.')
    
    def test_delete_blog_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('blog-delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Blog_Post.objects.filter(id=self.post.id).exists())


