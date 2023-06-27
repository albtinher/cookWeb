from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from cookweb.models import CategoriaCookie, ConfiguracionCookie, URL

class CookWebTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.cookies_url = reverse('cookies')
        self.configuraciones_url = reverse('configuraciones')
        self.websites_url = reverse('websites')

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 302) 

    def test_cookies_page(self):
        response = self.client.get(self.cookies_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookies.html')

    def test_configuraciones_page(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_login(user)
        response = self.client.get(self.configuraciones_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'configuraciones.html')

    def test_websites_page(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_login(user)
        response = self.client.get(self.websites_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websites.html')

    def test_post_configuraciones(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_login(user)


        categoria1 = CategoriaCookie.objects.create(nombre='Categoria 1')
        categoria2 = CategoriaCookie.objects.create(nombre='Categoria 2')

        response = self.client.post(reverse('configuracion_cookie_create'), {
            'nombre': 'Configuración de prueba',
            'categorias': [str(categoria1.id), str(categoria2.id)],
        })

        self.assertEqual(response.status_code, 302) 

        configuracion = ConfiguracionCookie.objects.filter(user=user, nombre='Configuración de prueba').first()
        self.assertIsNotNone(configuracion)
        self.assertEqual(configuracion.categoriasActivas.count(), 2)
        self.assertTrue(configuracion.activo)

    def test_websites_list(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_login(user)


        url = URL.objects.create(url='http://example.com', user=user)

        response = self.client.get(self.websites_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websites.html')
        self.assertContains(response, url.url)

    def test_delete_website(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_login(user)

        url = URL.objects.create(url='http://example.com', user=user)

        response = self.client.post(reverse('delete_website', args=[url.id]))
        self.assertEqual(response.status_code, 302)  

        url_exists = URL.objects.filter(id=url.id).exists()
        self.assertFalse(url_exists)


