# Generated by Django 3.0.8 on 2020-07-20 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0027_auto_20200720_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 19, 13, 5, 584780, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='personcomplaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 19, 13, 5, 586090, tzinfo=utc)),
        ),
    ]
