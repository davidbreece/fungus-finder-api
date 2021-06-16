from django.shortcuts import reverse
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient
from api.models import Mushroom
from django.contrib.auth.models import User


class TestFungusApi(APITestCase):
    def setUp(self):
        self.m1 = Mushroom.objects.create(
            id='1',
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

    def test_response(self):
        response = self.client.get(reverse('fungi'), format='json')
        self.assertEqual(len(response.data), 1)
        # assert a created status code was returned
        self.assertEqual(200, response.status_code)

    def test_get_fungi(self):
        response = self.client.get(reverse('fungi'), format="json")
        self.assertEqual(len(response.data), 1)
        #print(response.data)

    def test_updating_fungus(self):
        #user = User.objects.get(username='dbreece')
        client = APIClient()
        #client.login(username='dbreece', password='imDruid23!')

        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'id': '1',
            'name': 'Amanita musicalis',
            'image_link': 'https://en.wikipedia.org/wiki/Amanita_muscaria#/media/File:2006-10-25_Amanita_muscaria_crop.jpg',
            'wiki_link': 'https://en.wikipedia.org/wiki/Amanita_muscaria',
            'kingdom': 'Fungi',
            'division': 'Basidiomycota',
            'cclass': 'Agaricomycetes',
            'order': 'Agaricales',
            'family': 'Amanitaceae',
            'genus': 'Amanita',
            'species': 'A. muscaria alysia'
        }, format="json")
        # clprint(response.data)
        # items = list(response.items())
        print(response.data)
        self.assertEqual('Amanita musicalis', response.data['name'])

    def test_deleting_fungus(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))
        self.assertEqual(204, response.status_code)