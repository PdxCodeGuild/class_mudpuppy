# Generated by Django 3.0.8 on 2020-07-18 03:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0004_auto_20200718_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 18, 3, 44, 22, 628455, tzinfo=utc)),
        ),
    ]
