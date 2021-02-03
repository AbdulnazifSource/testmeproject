# Generated by Django 3.0.5 on 2020-10-31 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0019_auto_20201029_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiongroup',
            name='test_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testme.TestData'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionimages',
            name='test_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testme.TestData'),
            preserve_default=False,
        ),
    ]
