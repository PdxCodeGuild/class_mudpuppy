# Generated by Django 3.0.8 on 2020-07-17 03:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ball_pythons', '0007_ballpython_morph'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballpython',
            name='listed_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ballpython',
            name='morph',
            field=models.ManyToManyField(related_name='ballpythons', to='ball_pythons.Genetic'),
        ),
    ]
