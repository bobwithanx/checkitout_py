# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def catalog_to_item(apps, schema_editor):
    Item = apps.get_model("checkout", "Item")
    for item in Item.objects.all():
        item.image_name = item.catalog_item.image_name
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0043_auto_20160519_0005'),
    ]

    operations = [
        migrations.RunPython(catalog_to_item),
    ]
