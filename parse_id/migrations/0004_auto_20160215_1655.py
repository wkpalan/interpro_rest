# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse_id', '0003_auto_20160209_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id_desc',
            name='id_desc',
            field=models.CharField(max_length=1000),
        ),
    ]
