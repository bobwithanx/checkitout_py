# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_person_id_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='model',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='assigned_to',
            field=models.ForeignKey(blank=True, to='checkout.Person', null=True),
            preserve_default=True,
        ),
    ]
