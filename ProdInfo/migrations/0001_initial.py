# Generated by Django 2.2.5 on 2021-06-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.FloatField(default=0)),
                ('up_drop', models.FloatField(default=0)),
                ('up_drop_rate', models.FloatField(default=0)),
                ('trading_volumes', models.FloatField(default=0)),
                ('pub_time', models.DateTimeField(verbose_name='time published')),
            ],
        ),
    ]
