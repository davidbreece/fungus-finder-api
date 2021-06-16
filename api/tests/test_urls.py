from django.urls import reverse, resolve
from rest_framework.test import APITestCase


class TestAPIUrls(APITestCase):

    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail'
