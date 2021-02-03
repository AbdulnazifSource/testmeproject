# Generated by Django 3.0.5 on 2020-12-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0029_auto_20201221_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitegroup',
            old_name='created_by',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='sitegroup',
            name='total_users',
        ),
        migrations.AddField(
            model_name='sitegroup',
            name='general',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sitegroup',
            name='max_users',
            field=models.IntegerField(default=100),
        ),
    ]
