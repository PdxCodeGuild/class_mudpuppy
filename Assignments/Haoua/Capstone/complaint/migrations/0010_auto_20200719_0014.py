# Generated by Django 3.0.8 on 2020-07-19 00:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0009_auto_20200718_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 19, 0, 14, 32, 412638, tzinfo=utc)),
        ),
    ]