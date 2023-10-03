from django.test import TestCase
import datetime

from .models import AppUser

class AppUserModelTestCase(TestCase):
    def setUp(self):
        # Create a sample user for testing
        self.user = AppUser.objects.create(
            userName='testuser',
            firstName='John',
            lastName='Doe',
            email='test@example.com',
            birthDate='1990-01-01',
            location='Test Location',
            profilePicture='/static/profileImages/robot.jpg',
            isLoggedIn=False,
        )

    def test_user_creation(self):
        """
        Test that a user can be created with valid data.
        """
        self.assertEqual(AppUser.objects.count(), 1)
        saved_user = AppUser.objects.first()
        self.assertEqual(saved_user.userName, 'testuser')
        self.assertEqual(saved_user.firstName, 'John')
        self.assertEqual(saved_user.lastName, 'Doe')
        self.assertEqual(saved_user.email, 'test@example.com')
        self.assertEqual(saved_user.birthDate, datetime.date(1990, 1, 1))
        self.assertEqual(saved_user.location, 'Test Location')
        self.assertEqual(saved_user.profilePicture, '/static/profileImages/robot.jpg')
        self.assertFalse(saved_user.isLoggedIn)

    def test_user_str_representation(self):
        """
        Test the __str__ method of the user model.
        """
        self.assertEqual(str(self.user), 'testuser')