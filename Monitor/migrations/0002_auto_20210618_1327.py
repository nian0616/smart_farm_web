# Generated by Django 2.2.5 on 2021-06-18 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop_maturity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='environment_monitor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='monitor_video',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]