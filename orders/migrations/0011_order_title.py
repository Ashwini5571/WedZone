# Generated by Django 3.2.14 on 2022-07-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20220725_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
