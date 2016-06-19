# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def catalog_to_item(apps, schema_editor):
    Item = apps.get_model("checkout", "Item")
    for item in Item.objects.all():
        item.category_name = item.catalog_item.brand
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0035_auto_20160518_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category_name',
            field=models.ForeignKey(blank=True, to='checkout.Category', null=True),
            preserve_default=True,
        ),
    ]