# Generated by Django 3.0.7 on 2020-07-01 13:21

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20200701_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=User.models.upload_location),
        ),
    ]
