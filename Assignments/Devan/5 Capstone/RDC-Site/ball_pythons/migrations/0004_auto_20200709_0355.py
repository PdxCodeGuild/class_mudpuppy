# Generated by Django 3.0.8 on 2020-07-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ball_pythons', '0003_auto_20200709_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ballpython',
            name='picture',
            field=models.ImageField(upload_to='ball_pythons/img'),
        ),
    ]
