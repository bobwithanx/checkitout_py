# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20150308_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='person',
            new_name='student',
        ),
    ]
