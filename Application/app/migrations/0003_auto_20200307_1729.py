# Generated by Django 2.2.11 on 2020-03-07 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200307_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 17, 29, 2, 606815)),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 17, 29, 2, 606815)),
        ),
    ]