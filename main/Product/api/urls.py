from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Product.api.views import (
    ProductListView,
    TestView
)


app_name = 'product'

urlpatterns = [
    path('test/' , TestView.as_view() , name = 'list-api'), #bcoz it is class based view
    path('products/' , ProductListView.as_view() , name = 'list'), #bcoz it is class based view
]

