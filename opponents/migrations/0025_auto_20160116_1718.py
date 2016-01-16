# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opponents', '0024_auto_20160116_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='opponents_rating',
            new_name='rating',
        ),
    ]
