# Generated by Django 3.0.5 on 2020-10-24 18:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0015_auto_20201024_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionimages',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
