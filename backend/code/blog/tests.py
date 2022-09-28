from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetResponseTest(APITestCase):
    def test_get_response(self):
        """
        Ensure the URL/endpoint returns a 200 on a GET call
        """
        url = reverse("post-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
