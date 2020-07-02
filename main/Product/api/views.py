from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from Product.models import (
    Category,
    Room,
    RoomImages
)
from Product.api.serializers import (
    CategorySerializer,
    RoomsSerializer
)


class TestView(RetrieveAPIView):

    def get(self ,request , *args , **kwargs):
        data = Room.objects.get(pk=1)
        serializer = RoomsSerializer(data)
        return Response(serializer.data, status.HTTP_200_OK)
      

class ProductListView(ListAPIView):

    def get(self ,request , *args , **kwargs):
        data = Room.objects.all()
        serializer = RoomsSerializer(data , many=True)
        return Response(serializer.data, status.HTTP_200_OK)
      


