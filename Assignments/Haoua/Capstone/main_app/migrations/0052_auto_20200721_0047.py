# Generated by Django 3.0.8 on 2020-07-21 00:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0051_auto_20200720_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 0, 47, 38, 589058, tzinfo=utc)),
        ),
    ]
