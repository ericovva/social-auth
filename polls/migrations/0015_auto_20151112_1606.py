# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20151111_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default=b'Play and enjoy'),
        ),
        migrations.AddField(
            model_name='game',
            name='download_link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='play_link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(to='polls.Game'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='game',
            field=models.ForeignKey(to='polls.Game'),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='game',
            field=models.ForeignKey(to='polls.Game'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
