from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class vpsCreateTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.data = {
            "uid": '1998',
            "cpu": '2',
            "ram": '3',
            "hdd": '4',
            "status": "blocked"
        }
        self.createResponse = self.client.post(
            reverse('vps_create'),
            self.data,
            format="json")
        self.retrieveResponse = self.client.get(
            reverse('vps_retrieve', args=['1998']),
            format="json")

        self.listResponse = self.client.get(
            reverse('vps_list'),
            format="json")

    def test_creates_vps(self):
        self.assertEqual(self.createResponse.status_code, status.HTTP_201_CREATED)

    def test_retrieves_vps(self):
        self.assertEqual(self.retrieveResponse.status_code, status.HTTP_200_OK)

    def test_list_vps(self):
        self.assertEqual(self.listResponse.status_code, status.HTTP_200_OK)
