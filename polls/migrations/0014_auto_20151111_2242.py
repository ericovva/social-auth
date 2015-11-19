# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='user',
            field=models.ForeignKey(to='polls.MyUser', null=True),
        ),
        migrations.AddField(
            model_name='commentblogpost',
            name='user',
            field=models.ForeignKey(to='polls.MyUser', null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(to='polls.MyUser', null=True),
        ),
    ]
