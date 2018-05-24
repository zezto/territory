# Generated by Django 2.0.3 on 2018-05-13 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Terr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=100)),
                ('Owner', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='street',
            name='terr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Terr'),
        ),
    ]