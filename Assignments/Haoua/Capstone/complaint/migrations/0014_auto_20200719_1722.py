# Generated by Django 3.0.8 on 2020-07-19 17:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0013_auto_20200719_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 19, 17, 22, 26, 886569, tzinfo=utc)),
        ),
    ]
