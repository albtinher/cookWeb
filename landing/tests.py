from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('RegisterPage')

    def test_register(self):
        response = self.client.post(
            self.register_url,
            {
                'username': 'testuser',
                'name': 'Test',
                'surname': 'User',
                'email': 'test@example.com',
                'password': 'testpassword',
                'password_repeat': 'testpassword',
            }
        )
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(User.objects.count(), 1)  

    def test_login(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        response = self.client.post(
            reverse('AuthPage'),
            {
                'username': 'testuser',
                'password': 'testpassword',
            }
        )
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_login(user)
        response = self.client.get(reverse('LogOutPage'))
        self.assertEqual(response.status_code, 302) 
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        
    def test_home_page(self):
        response = self.client.get(reverse('MainPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainPage.html')

    def test_authenticated_user_access(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_login(user)
        response = self.client.get(reverse('MainPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainPage.html')


    def test_unauthenticated_user_access(self):
        response = self.client.get(reverse('MainPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainPage.html')


    def test_invalid_login(self):
        response = self.client.post(
            reverse('AuthPage'),
            {
                'username': 'invaliduser',
                'password': 'invalidpassword',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

