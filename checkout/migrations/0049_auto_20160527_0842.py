# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0048_auto_20160526_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='category',
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='time_requested',
        ),
    ]
