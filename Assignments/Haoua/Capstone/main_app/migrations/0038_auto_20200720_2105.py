# Generated by Django 3.0.8 on 2020-07-20 21:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0037_auto_20200720_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 21, 5, 56, 102626, tzinfo=utc)),
        ),
    ]
