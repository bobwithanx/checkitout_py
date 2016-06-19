# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0028_item_model_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='model_name',
            new_name='friendly_name',
        ),
    ]
