from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'Test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test1234')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'Test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
