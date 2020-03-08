# Generated by Django 2.2.11 on 2020-03-08 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200308_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='room_url',
            field=models.TextField(default='http://booking.com/123', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 8, 11, 44, 26, 746258)),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 8, 11, 44, 26, 746258)),
        ),
    ]
