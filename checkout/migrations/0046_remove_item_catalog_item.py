# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0045_auto_20160519_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='catalog_item',
        ),
    ]
