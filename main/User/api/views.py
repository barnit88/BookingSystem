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


# class UserAccountReteriveView(RetrieveAPIView):

#     def get(self ,request , *args , **kwargs):
#         try:
#             account = Account.objects.get(pk=2)
#         except Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         profile = account.profiles

#         if request.method == 'GET' :
#             serializer = ProfileSerializer(profile)
#             print(serializer.data)
#             return Response(serializer.data)

class UserAccountCreateView(CreateAPIView):

    def post(self ,request , *args , **kwargs):
        data= request.data       
        serializer = AccountCreateSerializer(data=data)
        if serializer.is_valid():
            a = serializer.save()
            data = give_token(a)
            return Response(data, status.HTTP_201_CREATED)
      
        return Response({"hello":"hello"})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer