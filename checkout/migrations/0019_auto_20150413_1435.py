# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0018_item_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255, null=True, blank=True)),
                ('image_name', models.CharField(max_length=255, null=True, blank=True)),
                ('brand', models.ForeignKey(to='checkout.Brand')),
                ('category', models.ForeignKey(to='checkout.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='item',
            field=models.ForeignKey(to='checkout.Catalog', null=True),
            preserve_default=True,
        ),
    ]
