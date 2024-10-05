from rest_framework.serializers import ModelSerializer
from kitten_show.models import Kitten


class KittenSerializer(ModelSerializer):

    class Meta:
        model = Kitten
        fields = ('id', 'name', 'color', 'age', 'breed', 'description')


class BreedsSerializer(ModelSerializer):

    class Meta:
        model = Kitten
        fields = ('id', 'name', 'breed',)
