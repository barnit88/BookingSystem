from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,PermissionsMixin

from django.db.models.signals import pre_save
from django.dispatch import receiver

import random
import string

# Create your models here.
def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def upload_location(instance , filename , **kwargs):
    print("-----------------------")
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id = str(instance.user.id),
        # title = str(randomString()),
        title = randomString(),
        filename = filename
    )
    return file_path

class MyAccountManager(BaseUserManager):
    def create_user(self,email , password = None):
        if not email:
            raise ValueError("User must have an email address")
       
        user = self.model(
            email = self.normalize_email(email),
            # name = name,
            # contact = contact,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self , email  , password  ):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            # name = name ,
            # contact = contact,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
        

class Account(AbstractBaseUser,PermissionsMixin):
    email                   = models.EmailField(verbose_name="email", max_length=60 ,unique=True)
    date_joined             = models.DateTimeField(verbose_name= 'date joined' ,auto_now_add=True)
    is_admin                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default = False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
  
    def __str__(self):
        return self.email
    
    def has_perm(self,perm , obj= None):
        return True

    def has_module_perms(self,app_label):
        return True


def image(instance):
    print("ayyo yaha")
    if instance.gender == "Male":
        return 'facebook.jpg'
    else:
        return 'female.jpg'


def set_avatar(instance):
    avatar = instance.image
    gender = instance.gender
    if gender == 'Male':
        avatar = 'facebook.jpg'
    else:
        avatar = 'female.jpg'
    return avatar

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]


class Profile(models.Model):
    user                    = models.OneToOneField(Account , 
        related_name='profiles',
        on_delete=models.CASCADE , 
        blank=True, null=True
        )
    name                    = models.CharField(max_length=45
        ,blank=True, null=True
        )
    contact                 = models.CharField(max_length=15)
    date_joined             = models.DateTimeField(
        verbose_name= 'date joined' ,
        auto_now_add=True
        )
    last_login              = models.DateTimeField(
        verbose_name='last login' ,
        auto_now=True
        )
    is_active               = models.BooleanField(default=True)
    image                   = models.ImageField(
        upload_to =upload_location ,
        blank=True, null=True
        )
    gender                  = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES
        )
    facebook_user           = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    

@receiver(pre_save, sender=Profile)
def post_save_avatar(sender, instance, *args, **kwargs):
     if not instance.image:
         instance.image = set_avatar(instance)


