from django.test import TestCase,SimpleTestCase
from django.contrib.auth import get_user_model
from .views import *
from unittest.mock import MagicMock, patch
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.test.client import Client, RequestFactory
#from django_mock_queries.query import MockSet, MockModel

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='anthon',
            email='antonchitay@gmail.com',
            password='testingpasscode123',
        )
        self.assertEqual(user.username,'anthon')
        self.assertEqual(user.email,'antonchitay@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='anthon',
            email='antonchitay@gmail.com',
            password='testingpasscode123',
        )
        self.assertEqual(user.username,'anthon')
        self.assertEqual(user.email,'antonchitay@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class AuthenticationTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Henry',
            email='henrisco@gmail.com', 
            password='testpass544'
        )
        user2 = User.objects.create_user(
            username='Henry2',
            email='henrisco2@gmail.com', 
            password='test4321dsfd'
        )

    def test_check_email(self):
        check_user = get_user_model().objects.all()[0]
        self.assertIn('@', check_user.email)
        self.assertIn('.com', check_user.email)
    
    def test_check_bad_email(self):
        check_user = get_user_model().objects.all()[1]
        self.assertNotIn(',', check_user.email)
        self.assertNotIn('!', check_user.email)
        self.assertNotIn('¡', check_user.email)
        self.assertNotIn('¿', check_user.email)
        self.assertNotIn('?', check_user.email)
        self.assertNotIn("'", check_user.email)
        self.assertNotIn('|', check_user.email)
        self.assertNotIn('°', check_user.email)
        self.assertNotIn('"', check_user.email)

    def test_check_duplicate_username(self):
        self.assertEqual(check_duplicate_username("Henry"), True)
    
    def test_check_duplicate_email(self):
        self.assertEqual(check_duplicate_username("invesntado@gmail.com"), False)
        
    def test_mock_create_user(self):
        with patch('users.models.CustomUser') as user_patch:
            mock_cp = MagicMock(spec=UsersListView)
            mock_cp.model.username = "HenryLeon"
            mock_cp.model.email = "henrisco@email.com"
            self.assertEqual(mock_cp.model.username, "HenryLeon")
            self.assertEqual(mock_cp.model.email, 'henrisco@email.com')


class ViewsProfile(SimpleTestCase):

    def view_profile(self):
        response = self.client.get('/Perfil/')
        self.assertEqual(response.status_code, 200)

class EditCustomTest(TestCase):
    def test_edit_custom(self):
        test_usuario = CustomUser.objects.create(username='alex', first_name='alexander', 
        last_name='ixvalan', email='alexnd@gmail.com',
        nacimiento='1995-12-12', password='la_password', dpi='6969958692359')

        usuario = CustomUser.objects.get(username=test_usuario.username)

        usuario.first_name = "alexanderXXX"
        usuario.last_name = "ixvalanXXX"

        usuario.save()

        self.assertEqual(usuario.username, 'alex')
        self.assertEqual(usuario.first_name, 'alexanderXXX')
        self.assertEqual(usuario.last_name, 'ixvalanXXX')
        self.assertEqual(usuario.email, 'alexnd@gmail.com')
        self.assertEqual(usuario.password, 'la_password')
        self.assertEqual(usuario.dpi, '6969958692359')


class LoginSuccess(TestCase):

    def setUp(self):
        self.client = Client()
        self.username="testuser"
        self.password="secret"
        CustomUser.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login(self):
        response = self.client.post(reverse('account_login'), {"login": self.username, "password": self.password}
        )
        self.assertEqual(response.status_code,200)

    def test_wrong_login(self):
        response = self.client.post(reverse('account_login'),
         {"login": "bad@login.com", "password": "wrong"}
        )
        validation_error = 'The e-mail address and/or password you specified are not correct'
        assert validation_error in response.content.decode('utf-8')