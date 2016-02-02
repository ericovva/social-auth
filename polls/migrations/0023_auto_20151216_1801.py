# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20151210_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='mark',
            field=models.FloatField(default=0),
        ),
    ]
