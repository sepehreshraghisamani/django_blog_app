from django.test import TestCase,SimpleTestCase

class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_home_page_template_used(self):
    #     response = self.client.get('/')
    #     self.assertTemplateUsed(response, 'pages/index.html')

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
