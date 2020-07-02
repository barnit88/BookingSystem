from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from User.api.views import (
    # UserAccountReteriveView,
    UserAccountCreateView,
    MyTokenObtainPairView
)

app_name = 'account'

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # path('<slug>/' , api_detail_blog_view , name = 'detail-api'),
    # path('<slug>/update/' , api_update_blog_view , name = 'update-api'),
    # path('<slug>/delete/' , api_delete_blog_view , name = 'delete-api'),
    # path('account/' , UserAccountReteriveView.as_view() , name = 'create-api'),
    path('list/' , UserAccountCreateView.as_view() , name = 'list-api'), #bcoz it is class based view
    path('login/' , MyTokenObtainPairView.as_view() , name = 'login'), #bcoz it is class based view
    
    # path('search' , ApiBlogSearchView.as_view() , name = 'search-api'),
]

