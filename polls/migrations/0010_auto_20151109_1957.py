# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20151109_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(to='polls.Post'),
        ),
    ]
