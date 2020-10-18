from django.test import TestCase,SimpleTestCase
from django.contrib.auth import get_user_model
from .views import *
from unittest.mock import MagicMock, patch

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