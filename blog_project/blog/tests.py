from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment
from django.utils import timezone

# Create your tests here.

class BlogAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.user1 = User.objects.create_user(username='user1', password='pass1234')
        self.user2 = User.objects.create_user(username='user2', password='pass1234')
        # Create posts
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.post1 = Post.objects.create(title='First Post', content='About Django', author=self.user1, created_at=timezone.now())
        self.post2 = Post.objects.create(title='Second Post', content='About Python', author=self.user2, created_at=timezone.now())
        self.post3 = Post.objects.create(title='Third Post', content='Django Filters', author=self.user1, created_at=timezone.now())

    def test_register(self):
        url = reverse('register')
        data = {'username': 'newuser', 'password': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_create_post_authenticated(self):
        token = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpass123'}).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(reverse('post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment_authenticated(self):
        token = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpass123'}).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        data = {'post': self.post.id, 'content': 'Great post!'}
        response = self.client.post(reverse('comment-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comments(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pagination_posts(self):
        response = self.client.get(reverse('post-list') + '?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)

    def test_search_posts(self):
        response = self.client.get(reverse('post-list') + '?search=Django')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any('Django' in post['title'] or 'Django' in post['content'] for post in response.data['results']))

    def test_filter_posts_by_author(self):
        response = self.client.get(reverse('post-list') + f'?author={self.user1.id}')
        self.assertEqual(response.status_code, 200)
        for post in response.data['results']:
            self.assertEqual(post['author'], self.user1.username)

    def test_ordering_posts(self):
        response = self.client.get(reverse('post-list') + '?ordering=title')
        self.assertEqual(response.status_code, 200)
        titles = [p['title'] for p in response.data['results']]
        self.assertEqual(titles, sorted(titles))

