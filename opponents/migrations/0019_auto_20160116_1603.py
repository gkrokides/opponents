# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0018_player_sprts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sports',
            field=models.ManyToManyField(default='', to='opponents.Sport', null=True, blank=True),
        ),
    ]
