# Generated by Django 3.0.7 on 2020-06-18 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemComplete',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='item_complete',
            field=models.BooleanField(default=False),
        ),
    ]