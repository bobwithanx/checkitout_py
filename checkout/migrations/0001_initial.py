# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('serial', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transactions',
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
        migrations.AddField(
            model_name='item',
            name='assigned_to',
            field=models.ForeignKey(to='checkout.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(to='checkout.Brand'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(to='checkout.Category'),
            preserve_default=True,
        ),
    ]
