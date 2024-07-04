# Generated by Django 5.0.6 on 2024-07-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.CharField(choices=[('', 'Destination'), ('Destination1', 'Destination1'), ('Destination2', 'Destination2'), ('Destination3', 'Destination3')], default='Destination', max_length=15),
        ),
        migrations.AddField(
            model_name='booking',
            name='duration',
            field=models.CharField(choices=[('', 'Duration'), ('Duration1', 'Duration1'), ('Duration2', 'Duration2'), ('Duration3', 'Duration3')], default='Duration', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_date',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='depart_date',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
