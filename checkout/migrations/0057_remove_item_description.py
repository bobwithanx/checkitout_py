# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0056_auto_20160527_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
    ]
