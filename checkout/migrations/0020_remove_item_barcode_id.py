# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_auto_20150413_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='barcode_id',
        ),
    ]
