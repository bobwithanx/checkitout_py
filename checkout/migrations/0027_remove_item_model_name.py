# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0026_auto_20160518_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='model_name',
        ),
    ]
