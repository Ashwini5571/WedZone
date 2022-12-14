# Generated by Django 3.2.14 on 2022-07-23 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('venue_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('guests', models.IntegerField(default=100)),
                ('venue_title', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('total_amount', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]
