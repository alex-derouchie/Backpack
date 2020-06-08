from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, profile
from django.contrib.auth import views as auth_views

class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register) 

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile) 

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView) 

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView) 

    def test_pass_reset_url_is_resolved(self):
        url = reverse('password_reset')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView) 

    def test_pass_reset_done_url_is_resolved(self):
        url = reverse('password_reset_done')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetDoneView) 

    def test_pass_reset_confirm_url_is_resolved(self):
        url = reverse('password_reset_confirm', args=['123', '456'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetConfirmView) 

    def test_pass_reset_complete_url_is_resolved(self):
        url = reverse('password_reset_complete')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetCompleteView) 