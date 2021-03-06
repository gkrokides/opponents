# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 08:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0025_auto_20160116_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player1', to='opponents.Player')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player2', to='opponents.Player')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opponents.Sport')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='opponents.Game'),
            preserve_default=False,
        ),
    ]
