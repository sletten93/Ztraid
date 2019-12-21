import json
from ..models import Product, Devices, ZtrUser, UserPref, FAQ, Paragraph
from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory, APIClient
from ..views import UsersViewSet, ProductViewSet, DevicesViewSet, UserPrefViewSet, FAQViewSet, ParagraphViewSet

# TODO - hitta extern bibliotek för mocking?
# TODO - hitta bra sätt att mocka DateTimeField för fält "created"


class BaseAppTestCase(APITestCase):

    def setUp(self):

        # TODO - avgöra om factory ska ersättas helt med client
        self.factory = APIRequestFactory()
        self.client = APIClient()

        self.viewUsers = UsersViewSet.as_view({'get': 'list'})
        self.viewProducts = ProductViewSet.as_view({'get': 'list'})
        self.viewDevices = DevicesViewSet.as_view({'get': 'list'})
        self.viewUserPref = UserPrefViewSet.as_view({'get': 'list'})
        self.viewFAQ = FAQViewSet.as_view({'get': 'list'})
        self.viewParagraph = ParagraphViewSet.as_view({'get': 'list'})

        self.viewUsersPost = UsersViewSet.as_view({'post': 'list'})
        self.viewProductPost = ProductViewSet.as_view({'post': 'list'})
        self.viewDevicesPost = DevicesViewSet.as_view({'post': 'list'})
        self.viewUserPrefPost = UserPrefViewSet.as_view({'post': 'list'})
        self.viewFAQPost = FAQViewSet.as_view({'post': 'list'})
        self.viewParagraphPost = ParagraphViewSet.as_view({'post': 'list'})

        self.uriUsers = '/Users/'
        self.uriProducts = '/Products/'
        self.uriDevices = '/Devices/'
        self.uriUserPref = '/UserPref/'
        self.uriFAQ = '/FAQ/'
        self.uriParagraph = '/Paragraph/'

        self.username1 = 'AdamUnitTest1'
        self.email1 = 'AdamUT1@unit.test'
        self.role1 = '1'
        self.nickname1 = 'AdamUTNickname1'
        self.phone1 = '111222333'
        self.salt1 = 'AdamUTSalt1'
        self.password1 = 'AdamUTPW1'

        self.username2 = 'AdamUnitTest2'
        self.email2 = 'AdamUT2@unit.test'
        self.role2 = '2'
        self.nickname2 = 'AdamUTNickname2'
        self.phone2 = '444555666'
        self.salt2 = 'AdamUTSalt2'
        self.password2 = 'AdamUTPW2'

        # En ZtrUser med 1-värden (ex username1) i alla fält
        ZtrUser.objects.create(name=self.username1, email=self.email1, role=self.role1, nickname=self.nickname1, phone=self.phone1, salt=self.salt1, password=self.password1)
        # En ZtrUser med 2-värden (ex username2) i alla fält förutom "role=self.role1"
        ZtrUser.objects.create(name=self.username2, email=self.email2, role=self.role1, nickname=self.nickname2, phone=self.phone2, salt=self.salt2, password=self.password2)

    def testZtrUser(self):
        user_1 = ZtrUser.objects.get(name='AdamUnitTest1')
        user_2 = ZtrUser.objects.get(name='AdamUnitTest2')

        self.assertEqual(user_1.get_role(), user_2.get_role())
        self.assertEqual(user_1.get_role(), '1')
        self.assertNotEqual(user_1.get_role(), '2')

        request = self.factory.get(self.uriUsers)
        response = self.viewUsers(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        params = {
            "name": "Post1User",
            "email": "email@the.email",
            "role": "1",
            "nickname": "nicknickname",
            "phone": "123"
            }
        response = self.client.post(self.uriUsers, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def testProduct(self):
        request = self.factory.get(self.uriProducts)
        response = self.viewProducts(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        params = {
            "name": "PostProduct1",
            "cost": "123.32"
        }
        response = self.client.post(self.uriProducts, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

        # testa FKs för ZtrUser
