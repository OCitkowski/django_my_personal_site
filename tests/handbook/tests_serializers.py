from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from handbook.serializers import SourceSerializer, OwnerSerializer, NoteSerializer
import requests


class SourceSerializerTestCase(APITestCase):
    def test_get(self):
        # url = reverse('note-list')
        # headers = {'Authentication': 'Bearer 03e24877ffd959815a174a958a1673d21f37698d'}
        # self.client.force_login(self.client.user)
        # response = self.client.get(url, headers=headers)
        # print(response.data)
        # self.owner1 = Owner.objects.create(name='Test1', comment='test_comment1')

        # url = 'http://127.0.0.1:8000/api/v1/'
        # headers = {'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'}
        # response = requests.get(url, headers=headers)
        print('Ok')
