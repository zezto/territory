# Generated by Django 2.1.4 on 2019-04-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190414_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='number',
            old_name='date_worked',
            new_name='date_worked1',
        ),
        migrations.AddField(
            model_name='number',
            name='date_worked2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='number',
            name='date_worked3',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
