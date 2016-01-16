# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0015_auto_20160116_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sports',
            field=models.ManyToManyField(default='Futsal', to='opponents.Sport', blank=True),
        ),
    ]
