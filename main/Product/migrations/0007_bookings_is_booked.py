# Generated by Django 3.0.7 on 2020-07-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_auto_20200708_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='is_booked',
            field=models.BooleanField(default=True),
        ),
    ]
