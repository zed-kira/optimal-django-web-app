# users/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def setUp(self):
        
        User = get_user_model()

        self.user = User.objects.create_user(
            username='zedkira',
            email='zedkira@email.com',
            password='testpass123'
        )

        self.admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )

    def test_create_user(self):

        self.assertEqual(self.user.username, 'zedkira')
        self.assertEqual(self.user.email, 'zedkira@email.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):

        self.assertEqual(self.admin_user.username, 'superadmin')
        self.assertEqual(self.admin_user.email, 'superadmin@email.com')
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)

