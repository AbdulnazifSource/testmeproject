# Generated by Django 3.0.5 on 2020-09-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaccount', '0002_auto_20200905_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='uploads/img/profile_pics/'),
        ),
    ]
