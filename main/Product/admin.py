from django.contrib import admin
from Product.models import (
    Category,
    Room,
    RoomImages,
    Test,
    Bookings
)

# Register your models here.

admin.site.register(Bookings)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(RoomImages)
admin.site.register(Test)

