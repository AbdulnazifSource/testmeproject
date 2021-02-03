# Generated by Django 3.0.5 on 2020-10-18 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='fill_answer_scheme',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testme.QuestionGroup'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testme.QuestionImages'),
        ),
        migrations.AlterField(
            model_name='questiongroup',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testme.QuestionImages'),
        ),
        migrations.AlterField(
            model_name='sitegroup',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitegroups', to=settings.AUTH_USER_MODEL),
        ),
    ]
