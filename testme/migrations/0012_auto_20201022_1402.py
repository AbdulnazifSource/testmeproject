# Generated by Django 3.0.5 on 2020-10-22 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0011_auto_20201022_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='options',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='testme.Question'),
        ),
        migrations.DeleteModel(
            name='QuestionOptions',
        ),
    ]
