from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer
from User.models import Profile
# from User.api.serializers import ProfileSerializer


class ProfileForTokenSerializer(ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['name' , 'image' ]
    


def give_token(user):
    context = {}
    refresh = RefreshToken.for_user(user)
    serializer = ProfileForTokenSerializer(user)
    context['refresh'] = str(refresh),
    context['access'] = str(refresh.access_token),
    context['profile'] = serializer.data    
    return context


