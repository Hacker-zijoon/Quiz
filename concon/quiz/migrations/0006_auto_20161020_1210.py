# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20161010_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='quiz/%Y/%m/%d'),
        ),
    ]