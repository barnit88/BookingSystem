from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from Product.models import (
    Category,
    Room,
    RoomImages
)


class ImageSerializer(ModelSerializer):

    class Meta:
        model = RoomImages
        fields = ['image']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['name' ,'price' ]


class RoomsSerializer(ModelSerializer):
    images   = ImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Room
        fields = ['name' ,'category' , 'images']

