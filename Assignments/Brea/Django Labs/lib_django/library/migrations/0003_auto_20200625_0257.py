# Generated by Django 3.0.7 on 2020-06-25 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_checkout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_Date',
            new_name='publish_date',
        ),
    ]