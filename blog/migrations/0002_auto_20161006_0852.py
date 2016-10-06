# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='No Title', max_length=200),
        ),
    ]
