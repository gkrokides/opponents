# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0019_auto_20160116_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='sprts',
        ),
    ]
