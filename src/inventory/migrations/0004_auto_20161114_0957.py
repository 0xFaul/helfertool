# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 08:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20161113_2325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useditem',
            options={'ordering': ('item__inventory__name', 'item__name', 'timestamp')},
        ),
    ]