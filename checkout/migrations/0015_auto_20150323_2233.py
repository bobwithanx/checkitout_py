# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20150323_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_out', models.DateTimeField()),
                ('time_in', models.DateTimeField()),
                ('item', models.ForeignKey(to='checkout.Item')),
                ('person', models.ForeignKey(to='checkout.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='time_in',
        ),
    ]
