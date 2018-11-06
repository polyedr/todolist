from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from .models import Todo_post


class Todo_postmodelTest(TestCase):
    
    
    def setUp(self):
        
        Todo_post.objects.create(title='just a test', author.pk=1)
        
    def test_text_content(self):
        todo_task=Todo_post.objects.get(id=1)        
        expected_object_title = str(todo_task.title)        
        self.assertEqual(expected_object_title, 'just a test')


class HomePageViewTest(TestCase):        


    def setUp(self):
        Todo_post.objects.create(text='this is another test', author.pk=1)
        
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

