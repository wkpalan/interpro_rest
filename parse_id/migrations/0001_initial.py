# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='id_desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db', models.CharField(max_length=100)),
                ('db_id', models.CharField(max_length=50)),
                ('id_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
