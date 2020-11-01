from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="just a text")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.title}"
        self.assertEqual(expected_object_name, 'just a text')


class HomeTest(TestCase):
    def setUp(self):
        Post.objects.create(title="this is a new test")

    def test_view_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'message/index.html')
