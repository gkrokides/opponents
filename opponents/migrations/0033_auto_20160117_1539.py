# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 13:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0032_auto_20160117_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
