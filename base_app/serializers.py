from rest_framework import serializers
from .models import Product, Devices, ZtrUser, UserPref, FAQ, Paragraph




class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'cost', 'created']


class DevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devices
        # Exempel på hur alla fält kan väljas enkelt
        fields = '__all__'


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
