# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0006_auto_20170109_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='upload_user_majoring',
            field=models.CharField(default='컴퓨터공학과', max_length=30),
        ),
        migrations.AddField(
            model_name='resume',
            name='upload_user_student_number',
            field=models.CharField(default='2015123456', max_length=30),
        ),
    ]
