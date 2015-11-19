# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_rating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='img',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
