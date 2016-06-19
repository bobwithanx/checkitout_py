# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0039_auto_20160518_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category_name',
        ),
    ]
