# Generated by Django 3.0.7 on 2020-07-05 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20200705_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Room')),
            ],
        ),
    ]
