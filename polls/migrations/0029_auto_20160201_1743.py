# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-01 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_auto_20160201_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='img',
            field=models.ImageField(null=True, upload_to=b'screenshots/'),
        ),
    ]
