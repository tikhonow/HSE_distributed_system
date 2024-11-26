from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Number

class NumberProcessorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_number_processing_success(self):
        response = self.client.post('/api/process-number/', {'number': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 6)
        self.assertTrue(Number.objects.filter(value=5).exists())

    def test_number_already_processed(self):
        Number.objects.create(value=5)
        response = self.client.post('/api/process-number/', {'number': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Number has already been processed.')

    def test_invalid_number_sequence(self):
        Number.objects.create(value=6)
        response = self.client.post('/api/process-number/', {'number': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['error'],
            'Invalid number sequence. Number 6 has already been processed.'
        )

    def test_negative_number(self):
        response = self.client.post('/api/process-number/', {'number': -1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Number must be a natural number (>= 0).', str(response.data))

    def test_non_integer_input(self):
        response = self.client.post('/api/process-number/', {'number': 'abc'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A valid integer is required.', str(response.data))
