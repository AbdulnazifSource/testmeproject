# Generated by Django 3.0.5 on 2020-12-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaccount', '0004_auto_20201121_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='image/profile_pics/'),
        ),
    ]
