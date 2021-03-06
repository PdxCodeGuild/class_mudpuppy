# Generated by Django 3.0.7 on 2020-07-01 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='birthday',
            name='char',
        ),
        migrations.AddField(
            model_name='birthday',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='birthday',
            name='sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='horoscope_app.Sign'),
        ),
    ]
