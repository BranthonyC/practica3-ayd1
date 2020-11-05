from django.test import TestCase,SimpleTestCase,override_settings, tag
from django.contrib.auth import get_user_model
from .views import *
from .models import *
from unittest.mock import MagicMock, patch
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.test.client import Client, RequestFactory
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
import os
import time
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
class MySeleniumTests(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']
    host = '0.0.0.0'

    @classmethod
    def setUpClass(cls):
        cls.host = "web"
        cls.selenium = webdriver.Remote(
            command_executor=os.environ['SELENIUM_HOST'],
            desired_capabilities=DesiredCapabilities.FIREFOX,
        )
        cls.selenium.implicitly_wait(10) 
        super(MySeleniumTests,cls).setUpClass()
    
    def setUp(self):
        self.browser = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX)
        User = get_user_model()
        self.user = User.objects.create_user(
            username='eddjavier',
            email='eddjavier@gmail.com',
            password='Tpasscode123',
        )

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    
    def test_login_E2E(self):
        print(self.live_server_url)
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_id("id_login")
        username_input.send_keys('eddjavier@gmail.com')
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys('Tpasscode123')
        current_url=self.selenium.current_url
        print(self.selenium.current_url)
        message_correo=username_input.get_attribute("validationMessage")
        message_password=password_input.get_attribute("validationMessage")
        boton1=self.selenium.find_element_by_xpath("//form[@id='form_id']/button[@class='btn btn-success']")
        boton1.click()
        self.assertEqual(message_correo,"")
        self.assertEqual(message_password,"")
        self.assertNotEqual(self.selenium.current_url,current_url)
        self.assertEqual(self.selenium.current_url,self.live_server_url+"/")
        print(self.selenium.current_url)
            
    def test_registry_E2E(self):
    
        print(self.live_server_url)
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup/'))
        email_input = self.selenium.find_element_by_id("id_email")
        email_input.send_keys('eddyjavier@gmail.com')
        first_name_input = self.selenium.find_element_by_id("id_first_name")
        first_name_input.send_keys('Eddy')
        last_name_input = self.selenium.find_element_by_id("id_last_name")
        last_name_input.send_keys('Sirin')
        nacimiento_input = self.selenium.find_element_by_id("id_nacimiento")
        #el = WebDriverWait(self.selenium, 20).until(EC.visibility_of_all_elements_located((By.ID, "id_nacimiento")))
        #el.clear()
        #el.send_keys("2020-02-12")
        nacimiento_input.click()
        nacimiento_input.send_keys('2020-11-20')
        dpi_input = self.selenium.find_element_by_id("id_dpi")
        dpi_input.send_keys('2959919600101')
        password_input = self.selenium.find_element_by_id("id_password1")
        password_input.send_keys('TestPassword123456')
        current_url=self.selenium.current_url
        print(self.selenium.current_url)
        print("text date: "+nacimiento_input.get_attribute("value"))
        message_correo=email_input.get_attribute("validationMessage")
        message_password=password_input.get_attribute("validationMessage")
        message_nacimiento=nacimiento_input.get_attribute("validationMessage")
        boton1=self.selenium.find_element_by_xpath("//form[@id='form_id']/button[@class='btn btn-success']")
        boton1.click()
        self.assertEqual(message_correo,"")
        self.assertEqual(message_password,"")
        self.assertEqual(message_nacimiento,"")
        self.assertNotEqual(self.selenium.current_url,current_url)
        self.assertEqual(self.selenium.current_url,self.live_server_url+"/")
        print(self.selenium.current_url)
        
#comentario
