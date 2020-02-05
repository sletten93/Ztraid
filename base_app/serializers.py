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
        # Exempel på hur alla fält kan väljas enkelt
        fields = '__all__'


class ZtrUserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="Ztraid:user-detail")

    class Meta:
        model = ZtrUser
        fields = ['url', 'id', 'username', 'email', 'password']
        write_only_fields = ('password',)
        read_only_fields = ('id',)

        # TODO - kolla säkerhetsnivån på lösningen
        def create(self, validated_data):
            user = ZtrUser.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
            )

            user.set_password(validated_data['password'])
            user.save()

            return user


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
