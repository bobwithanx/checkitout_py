# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('out_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('in_time', models.DateTimeField(null=True, blank=True)),
                ('item', models.ForeignKey(to='checkout.Item')),
                ('person', models.ForeignKey(to='checkout.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='item',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='person',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]
