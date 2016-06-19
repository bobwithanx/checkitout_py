# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0030_auto_20160518_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand_name',
            field=models.ForeignKey(blank=True, to='checkout.Brand', null=True),
            preserve_default=True,
        ),
    ]
