from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    SerializerMethodField
)

from User.models import (
    Account,
    Profile
)



class ProfileSerializer(ModelSerializer):
    # user = SerializerMethodField('get_email_from_user')

    class Meta:
        model = Profile
        fields = ['name' , 'image' ]
    
    # def get_email_from_user(self, profile):
    #     email = profile.user.email
    #     return email


class AccountSerializer(ModelSerializer):
    password = CharField(write_only='True')
    
    class Meta:
        model = Account
        # fields = ['email', 'profiles']
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
        return profile

