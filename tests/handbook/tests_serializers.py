from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from handbook.serializers import SourceSerializer, OwnerSerializer, NoteSerializer


class SourceSerializerTestCase(APITestCase):
    def test_get(self):
        url = reverse('note-list')
        # , kwargs = {'Authorization': 'Token 03e24877ffd959815a174a958a1673d21f37698d'}

        print( f'{url}  {type(self)}  *****************' )
        # response.set_cookie('Access_Token', str(refresh.access_token))
        # print(f'{self.client.cookies.} *****************')
        # ({'Authorization': 'Token 03e24877ffd959815a174a958a1673d21f37698d'})
        response = self.client.get(url)

        print(response)
        print(response.data)
        # self.owner1 = Owner.objects.create(name='Test1', comment='test_comment1')

