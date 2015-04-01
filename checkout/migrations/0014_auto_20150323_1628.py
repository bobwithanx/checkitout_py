# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_auto_20150321_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(blank=True, to='checkout.Item', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='person',
            field=models.ForeignKey(blank=True, to='checkout.Person', null=True),
            preserve_default=True,
        ),
    ]
