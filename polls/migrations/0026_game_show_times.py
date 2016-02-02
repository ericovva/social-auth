# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20151227_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='show_times',
            field=models.IntegerField(default=0),
        ),
    ]
