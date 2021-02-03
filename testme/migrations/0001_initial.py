# Generated by Django 3.0.5 on 2020-09-04 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('label', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GroupsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_number', models.IntegerField()),
                ('answer_type', models.CharField(choices=[('OPTION', 'option'), ('FILL', 'fill'), ('FILE', 'file')], max_length=6)),
                ('file_type', models.CharField(blank=True, choices=[('IMAGE', 'Image'), ('DOC', 'Doc'), ('PDF', 'Pdf')], max_length=6)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_answer', to='testme.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/img/question_images/')),
            ],
        ),
        migrations.CreateModel(
            name='SiteGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('total_users', models.IntegerField(default=0)),
                ('max_users', models.IntegerField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(through='testme.GroupsUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=11)),
                ('per_mark', models.IntegerField(default=1)),
                ('duration', models.IntegerField()),
                ('total_questions', models.IntegerField()),
                ('question_attemptable', models.IntegerField()),
                ('rewrite_test', models.BooleanField(default=True)),
                ('test_attempts', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('cover_image', models.FileField(upload_to='uploads/img/test_cover/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.SiteGroup')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.TestData')),
            ],
        ),
        migrations.AddField(
            model_name='testdata',
            name='group',
            field=models.ManyToManyField(through='testme.TestGroup', to='testme.SiteGroup'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_status', models.CharField(choices=[('Pending', 'pending'), ('Available', 'available')], max_length=9)),
                ('correct', models.IntegerField()),
                ('incorrect', models.IntegerField()),
                ('fill_data', models.TextField(blank=True)),
                ('upload_links', models.TextField(blank=True)),
                ('score', models.IntegerField()),
                ('grade', models.CharField(max_length=1)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('test_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.TestData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('header_note', models.TextField(blank=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.QuestionImages')),
                ('test_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.TestData')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.QuestionGroup'),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.QuestionImages'),
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.ManyToManyField(through='testme.QuestionOption', to='testme.Answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='test_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.TestData'),
        ),
        migrations.AddField(
            model_name='groupsuser',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testme.SiteGroup'),
        ),
        migrations.AddField(
            model_name='groupsuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
