# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followingqueryitem',
            name='query',
            field=models.TextField(),
        ),
    ]
