# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('polls', '0017_auto_20151113_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='game',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AddField(
            model_name='rating',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
