# Generated by Django 2.2.5 on 2021-06-18 14:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0003_auto_20210618_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment_monitor',
            name='time',
        ),
        migrations.AddField(
            model_name='environment_monitor',
            name='hour_time',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='crop_maturity',
            name='crop_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='crop_maturity',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='monitor_video',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='monitor_video',
            name='path',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='monitor_video',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
