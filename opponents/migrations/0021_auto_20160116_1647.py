# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0020_remove_player_sprts'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='players',
            field=models.ForeignKey(to='opponents.Player', null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='sports',
            field=models.ManyToManyField(to='opponents.Sport'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='opponents_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='self_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
