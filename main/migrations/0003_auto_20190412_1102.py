# Generated by Django 2.1.4 on 2019-04-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190407_0151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='number',
            options={'ordering': ['value']},
        ),
        migrations.AlterField(
            model_name='number',
            name='date_worked',
            field=models.DateField(auto_now=True),
        ),
    ]