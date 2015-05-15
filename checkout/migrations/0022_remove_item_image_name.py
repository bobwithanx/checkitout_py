# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0021_auto_20150512_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image_name',
        ),
    ]
