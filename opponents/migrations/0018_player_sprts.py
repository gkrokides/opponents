# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0017_auto_20160116_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sprts',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
    ]
