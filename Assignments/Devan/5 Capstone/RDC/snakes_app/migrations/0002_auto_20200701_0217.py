# Generated by Django 3.0.7 on 2020-07-01 02:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snakes_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snake',
            name='slug',
        ),
        migrations.AddField(
            model_name='snake',
            name='picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
