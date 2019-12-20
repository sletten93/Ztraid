import json
from ..models import Product, Devices, ZtrUser, UserPref, FAQ, Paragraph
from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate

# TODO - hitta extern bibliotek för mocking?
# TODO - hitta bra sätt att mocka DateTimeField för fält "created"


class BaseAppTestCase(APITestCase):

    def setUp(self):

        self.username1 = 'AdamUnitTest1'
        self.email1 = 'AdamUT1@unit.test'
        self.role1 = 1
        self.nickname1 = 'AdamUTNickname1'
        self.phone1 = '111222333'
        self.salt1 = 'AdamUTSalt1'
        self.password1 = 'AdamUTPW1'

        self.username2 = 'AdamUnitTest2'
        self.email2 = 'AdamUT2@unit.test'
        self.role2 = 2
        self.nickname2 = 'AdamUTNickname2'
        self.phone2 = '444555666'
        self.salt2 = 'AdamUTSalt2'
        self.password2 = 'AdamUTPW2'

        # En ZtrUser med 1-värden (ex username1) i alla fält
        ZtrUser.objects.create(name=self.username1, email=self.email1, role=self.role1, nickname=self.nickname1, phone=self.phone1, salt=self.salt1, password=self.password1)
        # En ZtrUser med 2-värden (ex username2) i alla fält förutom "role=self.role1"
        ZtrUser.objects.create(name=self.username2, email=self.email2, role=self.role1, nickname=self.nickname2, phone=self.phone2, salt=self.salt2, password=self.password2)

#        self.client.force_authenticate(user=self.user)

#  def test_1(self):
#       response = self.client.post('/snippets/', {'code': 'Foo Bar'}, format='json')
#        self.assertEqual(response.status_code, 201)

    def test1(self):
        ztr_user_1 = ZtrUser.objects.get(name='AdamUnitTest1')
        ztr_user_2 = ZtrUser.objects.get(name='AdamUnitTest2')

        self.assertEqual(ztr_user_1.get_role(), ztr_user_2.get_role())
        self.assertEqual(ztr_user_1.get_role(), '1')
        self.assertNotEqual(ztr_user_1.get_role(), '2')
