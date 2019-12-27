from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.serializers import StoreDataViewSerializer
from api.models import Store
# Create your tests here.

class InsertDataTestcase(APITestCase):

    def test_post_data(self):
        data = {"key1": "value1","key2": "value2"}
        response = self.client.post("/api/v1/values", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_data(self):
        data = {"key1": "value1","key2": "value2"}
        response = self.client.get("/api/v1/values", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_data(self):
        data = {"key1": "value1","key2": "value2"}
        response = self.client.patch("/api/v1/values", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    