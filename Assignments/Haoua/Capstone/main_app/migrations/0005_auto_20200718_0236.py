# Generated by Django 3.0.8 on 2020-07-18 02:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200718_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 18, 2, 36, 54, 415735, tzinfo=utc)),
        ),
    ]