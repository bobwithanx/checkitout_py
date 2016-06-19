# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0044_auto_20160519_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='catalog_item',
            field=models.ForeignKey(blank=True, to='checkout.Catalog', null=True),
            preserve_default=True,
        ),
    ]
