# Generated by Django 3.0.7 on 2020-06-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20200618_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='complete_date',
            field=models.DateTimeField(blank=True, verbose_name='date completed'),
        ),
    ]
