# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0013_auto_20160116_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sports',
            field=models.ManyToManyField(to='opponents.Sport', blank=True),
        ),
    ]
