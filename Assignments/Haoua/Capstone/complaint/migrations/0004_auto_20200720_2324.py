# Generated by Django 3.0.8 on 2020-07-20 23:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_auto_20200720_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 23, 24, 43, 493564, tzinfo=utc)),
        ),
        # migrations.AlterField(
        #     model_name='personcomplaint',
        #     name='date',
        #     field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 23, 24, 43, 494854, tzinfo=utc)),
        # ),
    ]
