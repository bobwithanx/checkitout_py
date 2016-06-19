# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0025_auto_20160518_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='display_name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='model_name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
