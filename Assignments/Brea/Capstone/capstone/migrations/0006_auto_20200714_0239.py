# Generated by Django 3.0.8 on 2020-07-14 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0005_auto_20200711_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews_qualityname', to='capstone.Quality'),
        ),
        migrations.AlterField(
            model_name='review',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='capstone.Song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
