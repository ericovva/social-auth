# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20151112_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentblogpost',
            name='post',
            field=models.ForeignKey(to='polls.BlogPost', null=True),
        ),
    ]
