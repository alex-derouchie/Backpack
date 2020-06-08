from django.test import TestCase
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

class TestForms(TestCase):

    #User Registration Form Tests
    def test_user_registration_form_valid_data(self):
        form = UserRegistrationForm(data={
            'username': 'TestUser1',
            'email': 'Test@test.com',
            'password1': 'TestPass1!',
            'password2': 'TestPass1!'
        })

        self.assertTrue(form.is_valid())
        print('user registration form valid data pass')

    def test_user_registration_form_no_data(self):
        form = UserRegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
        print('user registration form no data pass')

    #User Update Form Tests
    def test_user_update_form_valid_data(self):
        form = UserUpdateForm(data={
            'username': 'new username',
            'email': 'new@email.com'
        })

        self.assertTrue(form.is_valid())
        print('user update form valid data pass')

    def test_user_update_form_no_data(self):
        form = UserUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        print('user update form no data pass')

    #ProfileUpdateForm
    #idk about file loading here
    