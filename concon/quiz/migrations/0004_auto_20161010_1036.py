# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='result',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='result/%Y/%m/%d'),
        ),
    
    ]