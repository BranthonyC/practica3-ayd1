from django.test import TestCase
from django.contrib.auth import get_user_model
from .views import *

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