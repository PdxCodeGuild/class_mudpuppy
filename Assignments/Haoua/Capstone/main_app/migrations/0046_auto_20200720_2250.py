# Generated by Django 3.0.8 on 2020-07-20 22:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0045_auto_20200720_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 22, 50, 11, 920404, tzinfo=utc)),
        ),
    ]
