# Generated by Django 3.0.5 on 2020-10-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0009_auto_20201020_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
