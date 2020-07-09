from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
   RetrieveAPIView,
   CreateAPIView,
   UpdateAPIView
)
from rest_framework_simplejwt.views import TokenObtainPairView
from User.models import (
    Profile,
    Account
)
from User.api.jwtToken import give_token
from User.api.serializers import (
    AccountSerializer,
    AccountCreateSerializer,
    MyTokenObtainPairSerializer
)
import collections

class UserAccountReteriveView(RetrieveAPIView):

    def get(self ,request , *args , **kwargs):
        try:
            account = Account.objects.get(email='barnit@gmail.com')
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile = account.profiles

        if request.method == 'GET' :
            serializer = AccountCreateSerializer(profile)
            print(serializer.data)
            return Response(serializer.data)

    
class UserAccountCreateView(CreateAPIView,TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self ,request , *args , **kwargs):
        data= request.data
        print(data)
        serializer = AccountCreateSerializer(data=data)
        if serializer.is_valid():
            print('Validated')
            a = serializer.save()
            udata = request.data.pop('user')
            user = Account.objects.get(email=udata['email'])
            result = give_token(user)            
            return Response(result, status.HTTP_201_CREATED)
        return Response({"hello":"hello"})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

