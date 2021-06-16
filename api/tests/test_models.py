from django.shortcuts import reverse
from rest_framework.test import APITestCase
from unittest import TestCase
from unittest.mock import patch

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.test import Client
from django.test.client import RequestFactory

from api.models import Mushroom, WikiUrl
from api.scraping import Scraper
import api.scraping


class TestFungusModel(APITestCase):

    def setUp(self):
        self.m1 = Mushroom.objects.create(
            name='Amanita muscaria Alysia',
            image_link='https://en.wikipedia.org/wiki/Amanita_muscaria#/media/File:2006-10-25_Amanita_muscaria_crop.jpg',
            wiki_link='https://en.wikipedia.org/wiki/Amanita_muscaria',
            kingdom='Fungi',
            division='Basidiomycota',
            cclass='Agaricomycetes',
            order='Agaricales',
            family='Amanitaceae',
            genus='Amanita',
            species='A. muscaria alysia'
        )
        self.m1.save()
        self.scraper = Scraper()

    def tearDown(self):
        del self.m1

    def test_fungus_creation(self):
        self.assertEqual(Mushroom.objects.count(), 1)

    def test_fungus_representation(self):
        self.assertEqual(self.m1.name, str(self.m1))
