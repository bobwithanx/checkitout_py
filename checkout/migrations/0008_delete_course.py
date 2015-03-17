# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_student_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]
