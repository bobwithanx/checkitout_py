# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0057_remove_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='graduation_year',
            field=models.CharField(default=2017, max_length=4),
            preserve_default=False,
        ),
    ]
