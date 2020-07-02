from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
   RetrieveAPIView,
   CreateAPIView,
   UpdateAPIView
)
from User.models import (
    Profile,
    Account
)
from User.api.serializers import (
    ProfileSerializer,
    AccountSerializer,
    AccountCreateSerializer
)


class UserAccountReteriveView(RetrieveAPIView):

    def get(self ,request , *args , **kwargs):
        try:
            account = Account.objects.get(pk=2)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile = account.profiles

        if request.method == 'GET' :
            serializer = ProfileSerializer(profile)
            print(serializer.data)
            return Response(serializer.data)

class UserAccountCreateView(RetrieveAPIView):

    def post(self ,request , *args , **kwargs):
        data= request.data       
        serializer = AccountCreateSerializer(data=data)
        if serializer.is_valid():
            a = serializer.save()
            print("++===================")            
            print(a)
            return Response(serializer.data, status.HTTP_201_CREATED)
        # return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        # print(r["user['email']"])
        # try:
        #     account = Account.objects.get(pk=2)
        # except Profile.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        # profile = account.profiles

        # if request.method == 'GET' :
        #     serializer = AccountCreateSerializer(profile)
        return Response({"hello":"hello"})

