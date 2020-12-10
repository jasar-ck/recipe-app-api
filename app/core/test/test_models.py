from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with email successfull"""
        email = 'jas@jas.com'
        password = 'password'
        user = get_user_model().object.create_user(
            email = email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalization(self):
        """Test the email for a new user is normalized"""
        email = 'jas@JAS.COM'
        user = get_user_model().object.create_user(
            email, 'password'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test the email entered is invalid"""
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(
                None,'password'
            )

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().object.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
