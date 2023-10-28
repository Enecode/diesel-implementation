from django.test import TestCase
from . models import DieselData
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse


class DieselDataTestCase(TestCase):
    """Test case for diesel data model."""

    def setUp(self):
        """Create test data."""
        self.diesel_data = DieselData.objects.create(
            generator_id="01",
            fuel_level=0.0,
            timestamp="2023-10-28 00:00:00"
        )


    def test_diesel_data(self):
        """Test diesel data model."""
        self.assertEqual(self.diesel_data.generator_id, "01")
        self.assertEqual(self.diesel_data.fuel_level, 0.0)
        self.assertEqual(self.diesel_data.timestamp, "2023-10-28 00:00:00")

    def test_diesel_data_str(self):
        """Test diesel data model string representation."""
        self.assertEqual(str(self.diesel_data), "01 0.0 2023-10-28 00:00:00")
    
    def test_diesel_data_repr(self):
        """Test diesel data model string representation."""
        self.assertEqual(repr(self.diesel_data), "01 0.0 2023-10-28 00:00:00")

class test_that_users_can_register(TestCase):
    """Test that users can register."""

    def setUp(self):
        # Initialize the test client
        self.client = APIClient()

    def test_user_registration(self):
        registration_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
        }

        registration_url = reverse('register')

        response = self.client.post(registration_url, registration_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_that_an_existing_user_cannot_register(self):
        """Test that an existing user cannot register."""
        registration_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'email@email.com',
            'first_name': 'Test',
            'last_name': 'User',
        }
        registration_url = reverse('register')
        response = self.client.post(registration_url, registration_data, format='json')
        self.assertEqual(response.status_code, 201)
        response = self.client.post(registration_url, registration_data, format='json')
        self.assertEqual(response.status_code, 400)
    

class DieselDataListTestCase(TestCase):
    """Test case for diesel data list view."""

    def setUp(self):
        """Create test data."""
        self.diesel_data = DieselData.objects.create(
            generator_id="01",
            fuel_level=0.0,
            timestamp="2023-10-28 00:00:00"
        )
        self.client = APIClient()

    def test_diesel_data_list(self):
        """Test diesel data list view."""
        response = self.client.get(reverse('dieseldatalist'))
        self.assertEqual(response.status_code, 403)

    def test_diesel_data_list_is_authenticated(self):
        """Test diesel data list view."""
        self.client.force_authenticate(user=User.objects.create_user(username='testuser', password='12345'))
        response = self.client.get(reverse('dieseldatalist'))
        self.assertEqual(response.status_code, 200)

    def test_that_data_can_be_retrieved(self):
        """Test that data can be retrieved."""
        self.client.force_authenticate(user=User.objects.create_user(username='testuser', password='12345'))
        response = self.client.get(reverse('dieseldatalist'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)