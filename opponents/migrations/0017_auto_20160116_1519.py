# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0016_auto_20160116_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sports',
            field=models.ManyToManyField(default='', to='opponents.Sport', blank=True),
        ),
    ]
