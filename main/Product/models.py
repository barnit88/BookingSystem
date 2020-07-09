from django.db import models

import random
import string

from User.models import Profile
# Create your models here.

def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def upload_location(instance , filename , **kwargs):
    file_path = 'products/{category_id}/{room_id}/{title}-{filename}'.format(
        category_id = str(instance.room.category.id),
        room_id = str(instance.room.id),
        title = randomString(),
        filename = filename
    )
    return file_path



class Category(models.Model):
    name                    = models.CharField(max_length=45)
    price                   = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Room(models.Model):
    category                = models.ForeignKey(
        Category,
        related_name='rooms',
        on_delete=models.CASCADE)
    name                    = models.CharField(max_length=45
        )
    is_booked               = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class RoomImages(models.Model):
    room                    = models.ForeignKey(
        Room,
        related_name='images',
        on_delete=models.CASCADE )
    image                   = models.ImageField(
        upload_to =upload_location ,
        null=True,blank=True
        )
    
    
    def __str__(self):
        return self.room.name

    
class Bookings(models.Model):
    user                    = models.ForeignKey(
        Profile,
        related_name='user_bookings',
        null=True,
        on_delete=models.SET_NULL
    )
    room                    = models.ForeignKey(
        Room ,
        related_name='bookings',
        null=True,
        on_delete=models.SET_NULL)
    booked_date             = models.DateTimeField(auto_now_add=True)
    check_in                = models.DateTimeField()
    check_out               = models.DateTimeField()
    initial_payment         = models.IntegerField()    
    
    def __str__(self):
        return self.room.name + " is booked by " + self.user.name


# class Transaction(models.Model):
#     room                    = models.ForeignKey(
#         Room ,
#         related_name    = 'transactions' ,
#         on_delete       =models.SET_NULL ,
#         null=True
#         )
#     user                    = models.ForeignKey(
#         Profile,
#         related_name    ='user_transactions',
#         on_delete       = models.SET_NULL,
#         null=True
#         )
#     booking_date            = models.DateTimeField(auto_now_add=True)
#     check_in                = models.DateTimeField()
#     check_out               = models.DateTimeField()


class Test(models.Model):
    room                    = models.ForeignKey(
        Room ,
        related_name='test',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
