from django.contrib import admin
from django.urls import path , include
#for static and media files
from django.conf.urls.static import static
from django.conf import settings






urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api', ReterieveVeiw.as_view(), name='token_refresh'),
    path('api/account/', include('User.api.urls' , 'account')), #account api
    path('api/product/', include('Product.api.urls' , 'product')) #account api

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
