# Generated by Django 2.1.4 on 2019-04-30 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20190424_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='last_login',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='number',
            name='last_updated',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
