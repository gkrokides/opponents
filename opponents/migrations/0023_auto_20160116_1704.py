# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0022_auto_20160116_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='sports',
        ),
        migrations.AddField(
            model_name='player',
            name='sports',
            field=models.ForeignKey(blank=True, to='opponents.Sport', null=True),
        ),
    ]
