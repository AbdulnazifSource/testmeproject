# Generated by Django 3.0.5 on 2021-01-21 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0034_sitegroup_access_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitegroup',
            name='can_admit',
            field=models.BooleanField(default=True),
        ),
    ]
