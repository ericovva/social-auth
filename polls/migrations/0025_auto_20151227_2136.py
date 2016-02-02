# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_profilephoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='img',
            field=models.CharField(default=b'http://robohash.org/sitsequiquia.png?size=120x120', max_length=100),
        ),
    ]
