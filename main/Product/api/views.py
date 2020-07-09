from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from Product.models import (
    Category,
    Room,
    RoomImages,
    Bookings
)
from Product.api.serializers import (
    CategorySerializer,
    RoomsSerializer,
    ImageSerializer,
    BookingSerializer
)
from User.models import Profile
import collections

class TestView(ListAPIView):
    queryset            = RoomImages.objects.all() 
    serializer_class    = ImageSerializer
    # authentication_classes = (TokenAuthentication, ) #Allowany garda token chaindaina tyei ni samjhina lai rakhdeyko 
    permission_classes  = (AllowAny, ) #since it is tuple dont forget to add comma
    # pagination_class = PageNumberPagination    
    

    # def get(self ,request , *args , **kwargs):
    #     data = RoomImages.objects.all()
    #     serializer = ImageSerializer(data , many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
      

class ProductListView(ListAPIView):
    queryset                = Room.objects.all()
    serializer_class        = RoomsSerializer 
    authentication_classes  = (JWTAuthentication,)
    permission_classes      = (IsAuthenticated, ) #since it is tuple dont forget to add comma

    # def get(self ,request , *args , **kwargs):
    #     print("------------")
    #     print(request.data)
    #     print(request)
    #     data = Room.objects.all()
    #     serializer = RoomsSerializer(data , many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
      
# For uploading image 
# for test purpose only     
class ImageUpdateView(CreateAPIView):
    
    def post(self, request, *args, **kwargs):
        rid             = request.data.pop('id');
        data            = request.data;
        room            = Room.objects.get(pk=rid[0])
        imageInstance   = RoomImages(room=room)
        serializer      = ImageSerializer(imageInstance,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)       


class BookingCreateView(CreateAPIView):
    permission_classes      = (IsAuthenticated,)
    authentication_classes  = (JWTAuthentication,)

    def post(self, request, *args, **kwargs):
        print('---------------')
        pid             = request.user.profiles.id
        profile         = Profile.objects.get(pk=pid)
        rid             = request.data.pop('id')
        data            = request.data
        room            = Room.objects.get(pk=rid)
        if room.is_booked == False:        
            room.is_booked  = True
            room.save()
            booking         = Bookings(user = profile, room = room)
            serializer      = BookingSerializer(booking, data= data)
            if serializer.is_valid():
                print("-+_+_+_+_+__+_+_+_+_+_+_+_+_+__+")
                serializer.save()
                return Response(serializer.data , status.HTTP_201_CREATED)
        return Response({'Room' : 'Not Available'} ,status.HTTP_306_RESERVED)