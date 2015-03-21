# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_category_icon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Group',
        ),
        migrations.RenameModel(
            old_name='Student',
            new_name='Person',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='course',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='student',
            new_name='person',
        ),
        migrations.RemoveField(
            model_name='item',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='item',
            name='current_activity',
            field=models.ForeignKey(related_name='current_activity', blank=True, to='checkout.Transaction', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='out_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
