# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0023_auto_20150512_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
