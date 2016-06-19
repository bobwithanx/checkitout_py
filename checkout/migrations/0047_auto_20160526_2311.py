# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def data_change(apps, schema_editor):
    Item = apps.get_model("checkout", "Item")
    for item in Item.objects.filter(category__name="Media"):
        item.image_name = "dvd.png"
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0046_remove_item_catalog_item'),
    ]

    operations = [
        migrations.RunPython(data_change),
    ]
