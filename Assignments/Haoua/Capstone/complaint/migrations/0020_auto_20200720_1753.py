# Generated by Django 3.0.8 on 2020-07-20 17:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0019_auto_20200720_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 17, 53, 33, 514031, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='personcomplaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 17, 53, 33, 515404, tzinfo=utc)),
        ),
    ]