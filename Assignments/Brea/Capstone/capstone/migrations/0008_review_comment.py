# Generated by Django 3.0.8 on 2020-07-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0007_auto_20200715_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
