# Generated by Django 3.2.14 on 2022-07-21 05:26

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_venue_venue_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='venue',
            name='amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Parking Area', 'Parking Area'), ('Air Conditioning', 'Air Conditioning'), ('CCTV', 'CCTV')], max_length=100),
        ),
    ]
