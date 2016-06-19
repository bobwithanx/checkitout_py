# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def catalog_to_item(apps, schema_editor):
    Item = apps.get_model("checkout", "Item")
    for item in Item.objects.all():
        item.brand_name = item.catalog_item.brand
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0032_auto_20160518_2252'),
    ]

    operations = [
        migrations.RunPython(catalog_to_item),
    ]
