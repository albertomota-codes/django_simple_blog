# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.TextField()),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
