# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20151109_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='text',
            new_name='description',
        ),
    ]
