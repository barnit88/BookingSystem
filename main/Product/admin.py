from django.contrib import admin
from Product.models import (
    Category,
    Room,
    RoomImages
)

# Register your models here.

admin.site.register(Category)
admin.site.register(Room)
admin.site.register(RoomImages)

