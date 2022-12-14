# Generated by Django 3.2.14 on 2022-07-24 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20220724_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decorator',
            name='booked_for',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='dj',
            name='booked_for',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='makeup',
            name='booked_for',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='mehndi',
            name='booked_for',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='pandit',
            name='booked_for',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='transport',
            name='booked_for',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='weddingplanner',
            name='booked_for',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime),
        ),
    ]
