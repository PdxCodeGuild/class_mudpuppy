# Generated by Django 3.0.7 on 2020-07-01 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakes_app', '0002_auto_20200701_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake',
            name='picture',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
