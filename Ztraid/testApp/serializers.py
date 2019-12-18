from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product, Devices, ZtrUser, UserPref, FAQ, Paragraph


# TODO - avgöra om vi önskar använda hyperlinking, PKs eller något annat för att hantera entitets-relationer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'name', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'cost']


class DevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devices
        fields = ['url', 'id', 'name', 'OS', 'GPU', 'CPU', 'cam', 'mic']


class ZtrUserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="testapp:user-detail")

    class Meta:
        model = ZtrUser
        fields = ['url', 'id', 'name', 'email', 'role', 'nickname', 'phone']


class UserPrefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPref
        fields = ['url', 'id', 'user_ID', 'net_speed']


class FAQSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FAQ
        fields = ['url', 'id', 'question', 'answer', 'example']

class ParagraphSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['url', 'id', 'text']
