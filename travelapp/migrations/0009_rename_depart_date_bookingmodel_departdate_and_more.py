# Generated by Django 5.0.6 on 2024-07-03 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0008_rename_booking_bookingmodel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingmodel',
            old_name='depart_date',
            new_name='departDate',
        ),
        migrations.RenameField(
            model_name='bookingmodel',
            old_name='return_date',
            new_name='returnDate',
        ),
    ]
