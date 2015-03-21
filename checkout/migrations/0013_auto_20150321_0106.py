# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20150320_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='in_time',
            new_name='time_in',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='out_time',
            new_name='time_out',
        ),
        migrations.AddField(
            model_name='transaction',
            name='time_requested',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
