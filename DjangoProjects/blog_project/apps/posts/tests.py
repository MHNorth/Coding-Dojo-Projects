from django.test import TestCase
from .models import UserPost

class PostModelTest(TestCase):

    def setUp(self):
        UserPost.objects.create(text='just a test')

    def test_test_content(self):
        post=UserPost.objects.get(id=1)
        expected_object_name =  '{}'.format(post.text)
        self.assertEqual(expected_object_name, 'just a test')