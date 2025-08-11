from django.test import TestCase
from django.urls import reverse


from .models import Post


# class PostTestCase(TestCase):

#     def setUp(self):
#         self.post = Post.objects.create(title="Test Post", content="This is a test post.")

#     def test_post_creation(self):
 
#         self.assertIsInstance(self.post, Post)
#         self.assertEqual(self.post.title, "Test Post")
#         self.assertEqual(self.post.content, "This is a test post.")

# Create your tests here.

class Post_list_view_test(TestCase):
    def setUp(self):
        Post.objects.create(title="Test Post 1", content="Content for test post 1")

    def test_post_list_view(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post 1")
    def test_post_list_view_url(self):
        response = self.client.get(reverse('list_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/list.html')

        



