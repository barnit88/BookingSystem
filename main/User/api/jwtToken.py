from rest_framework_simplejwt.tokens import RefreshToken
from User.api.serializers import ProfileSerializer

def get_tokens_for_user(user):
    context = {}
    refresh = RefreshToken.for_user(user)
    data = ProfileSerializer(user)
    context['refresh'] = str(refresh),
    context['access'] = str(refresh.access_token),
    context['profile'] = data.data
    
    return context