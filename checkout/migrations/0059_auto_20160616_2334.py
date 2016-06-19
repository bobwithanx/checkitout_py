# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0058_person_graduation_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
