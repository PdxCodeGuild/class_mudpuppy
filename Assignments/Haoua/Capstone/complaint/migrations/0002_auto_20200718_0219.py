# Generated by Django 3.0.8 on 2020-07-18 02:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 18, 2, 19, 30, 979235, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='address',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='business',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
