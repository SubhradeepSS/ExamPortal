# Generated by Django 3.0.6 on 2020-05-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0004_auto_20200520_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_db',
            name='answer',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
