# Generated by Django 3.2.14 on 2022-07-31 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('service_type', models.CharField(choices=[('Photographer', 'Photographer'), ('Venue', 'Venue'), ('Caterer', 'Caterer'), ('Decorator', 'Decorator'), ('Makeup', 'Makeup'), ('Mehndi', 'Mehndi'), ('Pandit', 'Pandit'), ('Transport', 'Transport'), ('DJ', 'DJ'), ('Wedding planner', 'Wedding planner')], max_length=100)),
                ('vendor_id', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Madhaya Pradesh', 'Madhaya Pradesh'), ('Kerala', 'Kerala'), ('Karnataka', 'Karnataka'), ('Maharashtra', 'Maharashtra'), ('Punjab', 'Punjab'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand')], max_length=100)),
                ('featured_package_price', models.IntegerField()),
                ('service_photo', models.FileField(upload_to='photos/%y/%m/%d/')),
                ('service_photo_1', models.FileField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('service_photo_2', models.FileField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('service_photo_3', models.FileField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('service_photo_4', models.FileField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('other_details', models.TextField(blank=True, max_length=500)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]