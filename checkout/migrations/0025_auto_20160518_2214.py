# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0024_person_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-active', 'id_number'], 'verbose_name_plural': 'people'},
        ),
        migrations.AlterModelOptions(
            name='transactionhistory',
            options={'verbose_name_plural': 'transaction histories'},
        ),
        migrations.AlterField(
            model_name='item',
            name='inventory_tag',
            field=models.CharField(default=datetime.datetime(2016, 5, 18, 22, 14, 50, 520451), max_length=255),
            preserve_default=False,
        ),
    ]
