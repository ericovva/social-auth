# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151109_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='description',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='description',
        ),
    ]
