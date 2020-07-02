from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    SerializerMethodField
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from User.models import (
    Account,
    Profile
)
from User.api.jwtToken import give_token



class AccountSerializer(ModelSerializer):
    password = CharField(write_only='True')
    
    class Meta:
        model = Account
        fields = ['email' ,'password']

class AccountCreateSerializer(ModelSerializer):
    user = AccountSerializer(write_only = 'True')

    class Meta:
        model = Profile
        fields = ['name' ,'contact' , 'image', 'gender' , 'user']

    def create(self, validated_data):
        d = validated_data.pop('user')
        user = dict(d)
        email=user['email']
        account = Account.objects.create(email=email)
        account.set_password(user['password'])
        account.save()
        profile = Profile.objects.create(**validated_data)
        profile.user = account
        profile.save()
        return profile

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self,attr):
        # print(attr) #login credentials are obtained
        user = dict(attr)
        # data = super().validate(attr)  yesare attribute pass garda data leh token pair dinxa
        email = user['email']
        account = Account.objects.get(email=email)
        profile = account.profiles
        data = give_token(profile)
        print(data['refresh'][0])
        return data

