# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0038_auto_20160518_2312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['display_name']},
        ),
        migrations.RemoveField(
            model_name='item',
            name='friendly_name',
        ),
    ]
