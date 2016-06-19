# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def catalog_to_item(apps, schema_editor):
    Item = apps.get_model("checkout", "Item")
    for item in Item.objects.all():
        item.category_name = item.catalog_item.category
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0036_item_category_name'),
    ]

    operations = [
        migrations.RunPython(catalog_to_item),
    ]
