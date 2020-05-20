# Generated by Django 3.0.6 on 2020-05-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_question_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_db',
            name='answer',
        ),
        migrations.AddField(
            model_name='question_db',
            name='optionA',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_db',
            name='optionB',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_db',
            name='optionC',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_db',
            name='optionD',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
    ]
