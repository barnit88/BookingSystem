# Generated by Django 3.0.7 on 2020-07-05 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_auto_20200702_2325'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedroom',
            name='is_booked',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bookedroom',
            name='room',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='Product.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='Product.Category'),
        ),
        migrations.AlterField(
            model_name='roomimages',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Product.Room'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='Product.Room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_transactions', to='User.Profile')),
            ],
        ),
    ]
