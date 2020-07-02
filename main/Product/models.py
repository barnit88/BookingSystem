from django.db import models
import random
import string
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
    
    def __str__(self):
        return self.name



class RoomImages(models.Model):
    room                    = models.ForeignKey(
        Room,
        related_name='images',
        on_delete=models.CASCADE )
    image                   = models.ImageField(
        upload_to =upload_location 
        )
    
    
    def __str__(self):
        return self.room.name

    
class BookedRoom(models.Model):
    room                    = models.OneToOneField(
        Room ,
        related_name='bookings',
        on_delete=models.CASCADE)
    booked_date             = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.room.name + " " + self.booked_date
