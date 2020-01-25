from rest_framework import viewsets, generics
from base_app.serializers import ZtrUserSerializer, ProductSerializer, DevicesSerializer, UserPrefSerializer, FAQSerializer, ParagraphSerializer
from .models import Product, Devices, ZtrUser, UserPref, FAQ, Paragraph


class UsersViewSet(viewsets.ModelViewSet):

    queryset = ZtrUser.objects.all()
    serializer_class = ZtrUserSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DevicesViewSet(viewsets.ModelViewSet):

    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class UserPrefViewSet(viewsets.ModelViewSet):

    queryset = UserPref.objects.all()
    serializer_class = UserPrefSerializer


class FAQViewSet(viewsets.ModelViewSet):

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ParagraphViewSet(viewsets.ModelViewSet):

    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

