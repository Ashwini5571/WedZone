# Generated by Django 3.2.14 on 2022-07-21 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_photographer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
