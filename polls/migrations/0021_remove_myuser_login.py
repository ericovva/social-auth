# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_myuser_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='login',
        ),
    ]
