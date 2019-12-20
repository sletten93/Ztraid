from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Ztraid.testApp.serializers import UserSerializer, GroupSerializer, ZtrUserSerializer, ProductSerializer, DevicesSerializer, UserPrefSerializer, FAQSerializer, ParagraphSerializer
from .models import Product, Devices, ZtrUser, UserPref, FAQ, Paragraph


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ZtrUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ZtrUser.objects.all()
    serializer_class = ZtrUserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DevicesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class UserPrefViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserPref.objects.all()
    serializer_class = UserPrefSerializer


class FAQViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ParagraphViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
