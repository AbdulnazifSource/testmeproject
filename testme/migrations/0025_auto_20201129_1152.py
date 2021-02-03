# Generated by Django 3.0.5 on 2020-11-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0024_testdata_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='finish_timeinsec',
        ),
        migrations.AddField(
            model_name='result',
            name='finish_time',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='correct',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='grade',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='result',
            name='incorrect',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='result_status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Available', 'available')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(blank=True),
        ),
    ]
