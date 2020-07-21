# Generated by Django 3.0.8 on 2020-07-20 21:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaint', '0030_auto_20200720_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='name',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='personcomplaint',
            name='name',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 21, 2, 51, 829149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='personcomplaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 21, 2, 51, 830463, tzinfo=utc)),
        ),
    ]
