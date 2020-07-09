from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from Product.models import (
    Category,
    Room,
    RoomImages,
    Test,
    Bookings
)

class BookingSerializer(ModelSerializer):

    class Meta:
        model = Bookings
        fields = [ 'check_in' , 'check_out' , 'initial_payment']


class ImageSerializer(ModelSerializer):
    # room = RoomManage(write_only=True)

    class Meta:
        model = RoomImages
        fields = ['image']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['name' ,'price' ]


class TestSerializer(ModelSerializer):

    class Meta:
        model = Test
        fields = ['name']
        

class RoomsSerializer(ModelSerializer):
    images   = ImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    test    = TestSerializer(read_only=True, many=True) 

    class Meta:
        model = Room
        fields = ['id' , 'name' ,'is_booked','category' , 'images' ,'test']

