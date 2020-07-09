from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Product.api.views import (
    ProductListView,
    TestView,
    ImageUpdateView,
    BookingCreateView
)


app_name = 'product'

urlpatterns = [
    path('test/' , TestView.as_view() , name = 'test-api'), #bcoz it is class based view
    path('products/' , ProductListView.as_view() , name = 'prod'), #bcoz it is class based view
    path('update/' , ImageUpdateView.as_view() , name = 'update'), #bcoz it is class based view
    path('booking/', BookingCreateView.as_view() , name = 'booking')
]


