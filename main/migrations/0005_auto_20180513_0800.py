# Generated by Django 2.0.3 on 2018-05-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180513_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='terr',
            name='lat_cordinate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='terr',
            name='long_cordinate',
            field=models.FloatField(default=0),
        ),
    ]
