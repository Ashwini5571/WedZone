# Generated by Django 3.2.14 on 2022-07-21 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_venue_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='venue_description',
        ),
    ]
