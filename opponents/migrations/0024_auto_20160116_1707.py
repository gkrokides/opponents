# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0023_auto_20160116_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='self_rating',
        ),
        migrations.AddField(
            model_name='player',
            name='self_rating',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=False,
        ),
    ]
