# Generated by Django 3.0.8 on 2020-07-19 23:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20200719_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 19, 23, 19, 53, 591542, tzinfo=utc)),
        ),
    ]
