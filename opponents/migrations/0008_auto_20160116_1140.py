# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0007_auto_20160116_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='sport',
            new_name='sports',
        ),
    ]
