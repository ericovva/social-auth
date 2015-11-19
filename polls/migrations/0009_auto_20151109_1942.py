# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20151109_1936'),
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
        migrations.RemoveField(
            model_name='game',
            name='download_link',
        ),
        migrations.RemoveField(
            model_name='game',
            name='play_link',
        ),
        migrations.AddField(
            model_name='post',
            name='download_link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='play_link',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
