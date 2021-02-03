# Generated by Django 3.0.5 on 2020-11-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0022_auto_20201121_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdata',
            name='group',
        ),
        migrations.AddField(
            model_name='sitegroup',
            name='tests',
            field=models.ManyToManyField(through='testme.TestGroup', to='testme.TestData'),
        ),
    ]
