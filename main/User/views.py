from django.shortcuts import render
# from User.models import Profile
# # from rest_framework.generics import (
# #     RetrieveAPIView,
# #     ListAPIView
# # )
# # from rest_framework.permissions import IsAuthenticated
# # from django.contrib.auth.models import User
# # from User.api.serializers import Serial
# # # Create your views here.
# # from rest_framework_simplejwt.tokens import RefreshToken
# # from User.models import Profile
# # from rest_framework.response import Response
# # from rest_framework.decorators import api_view ,permission_classes

# # def get_tokens_for_user(user):
# #     refresh = RefreshToken.for_user(user)
# #     print("Hello")
# #     return {
# #         'refresh': str(refresh),
# #         'access': str(refresh.access_token),
# #     }
    
# # class ReterieveVeiw(ListAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = Serial
# #     permission_classes = [IsAuthenticated]

# # @api_view(['GET',])
# # def tokens(request):
# #     x = Profile.objects.get(pk=3)
# #     a = get_tokens_for_user(x)
# #     return Response(a)

# def userlist(request):
#     context = {}
#     a = Profile.objects.all()
#     context['a'] = a

#     return render(request,'User/hello.html' , context)


