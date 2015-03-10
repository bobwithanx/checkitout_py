# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20150307_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id_number',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
