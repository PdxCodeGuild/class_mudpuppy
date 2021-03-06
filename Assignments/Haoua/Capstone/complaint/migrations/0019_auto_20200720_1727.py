# Generated by Django 3.0.8 on 2020-07-20 17:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaint', '0018_auto_20200719_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 17, 27, 30, 141785, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='name',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PersonComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('perpetrator', models.CharField(max_length=300)),
                ('job_phone', models.CharField(max_length=200)),
                ('job_email', models.EmailField(max_length=254)),
                ('job', models.CharField(max_length=300)),
                ('social_media', models.CharField(max_length=400)),
                ('review', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 7, 20, 17, 27, 30, 143208, tzinfo=utc))),
                ('name', models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
