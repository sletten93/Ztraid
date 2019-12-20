from rest_framework import serializers
from .models import Product, Devices, ZtrUser, UserPref, FAQ, Paragraph


# TODO - avgöra om vi önskar använda hyperlinking, PKs eller något annat för att hantera entitets-relationer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'cost', 'created']


class DevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devices
        fields = ['url', 'id', 'name', 'OS', 'GPU', 'CPU', 'cam', 'mic', 'created']


class ZtrUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZtrUser
        fields = ['url', 'id', 'name', 'email', 'role', 'nickname', 'phone', 'created']


class UserPrefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPref
        fields = ['url', 'id', 'user_ID', 'net_speed', 'created']


class FAQSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FAQ
        fields = ['url', 'id', 'question', 'answer', 'example', 'created']


class ParagraphSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['url', 'id', 'text', 'created']
