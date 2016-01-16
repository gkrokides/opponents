# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0021_auto_20160116_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='players',
        ),
        migrations.AlterField(
            model_name='player',
            name='sports',
            field=models.ManyToManyField(default='', to='opponents.Sport', null=True, blank=True),
        ),
    ]
