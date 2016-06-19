# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def data_change(apps, schema_editor):
    Item = apps.get_model("checkout", "Item")
    for item in Item.objects.filter(description=None):
        #item.display_name = '%s (%s)' % (item.display_name, item.description)
        #item.display_name = item.display_name[:-3]
        item.discription = "none"
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0050_auto_20160527_0857'),
    ]

    operations = [
        migrations.RunPython(data_change),
    ]
