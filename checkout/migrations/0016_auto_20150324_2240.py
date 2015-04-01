# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_auto_20150323_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='current_activity',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(to='checkout.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='person',
            field=models.ForeignKey(to='checkout.Person'),
            preserve_default=True,
        ),
    ]
