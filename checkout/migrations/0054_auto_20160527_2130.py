# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def data_change(apps, schema_editor):
    Item = apps.get_model("checkout", "Item")
    for item in Item.objects.filter(description__isnull=True):
        #item.display_name = '%s (%s)' % (item.display_name, item.description)
        #item.display_name = item.display_name[:-3]
        item.discription = 'x'
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0053_auto_20160527_2127'),
    ]

    operations = [
        migrations.RunPython(data_change),
    ]
