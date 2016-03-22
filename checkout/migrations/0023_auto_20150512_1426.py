# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0022_remove_item_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='model',
        ),
    ]
