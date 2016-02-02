# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_auto_20151216_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_src', models.TextField(max_length=10000)),
                ('user', models.ForeignKey(to='polls.MyUser', null=True)),
            ],
        ),
    ]
