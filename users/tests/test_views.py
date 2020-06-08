from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='TestingUser',
            email='test@testing.com',
            password='Password123'
        )

        self.register_url = reverse('register')
        self.profile_url = reverse('profile')

    #Register View Tests
    def test_register_view_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        print('register view GET pass')

    def test_register_view_POST_creates_user(self):
        response = self.client.post(self.register_url, {
            'username':'RegTestUser',
            'email': 'regtest@user.com',
            'password1': 'APassword1!',
            'password2': 'APassword1!'
        })       

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.filter(username='RegTestUser').count(), 1)
        print('register view POST pass')

    def test_register_view_POST_no_data(self):
        response = self.client.post(self.register_url)       

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.filter(username='RegTestUser').count(), 0)
        print('register view POST no data pass')

    #Profile View Tests
    def test_profile_view_GET(self):
        self.client.force_login(user=self.test_user) #Profile has an @loginrequired tag
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
        print('profile view GET pass')

    def test_profile_view_POST_updates_profile(self):
        self.client.force_login(user=self.test_user) #Profile has an @loginrequired tag
        response = self.client.post(self.profile_url, {
            'username':'UPDATEDTestUser',
            'email': 'updatedregtest@user.com'
        })       

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.filter(username='UPDATEDTestUser').count(), 1)
        print('profile view POST pass')

    def test_profile_view_POST_no_data(self):
        self.client.force_login(user=self.test_user) #Profile has an @loginrequired tag
        response = self.client.post(self.profile_url)       

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.filter(username='TestingUser').count(), 1)
        print('profile view POST no data pass')