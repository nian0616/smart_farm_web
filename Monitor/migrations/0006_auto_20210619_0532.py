# Generated by Django 2.2.5 on 2021-06-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0005_auto_20210619_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment_monitor',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='environment_monitor',
            name='hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='environment_monitor',
            name='month',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='environment_monitor',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
