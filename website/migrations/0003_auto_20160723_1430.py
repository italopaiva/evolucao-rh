# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160709_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='requester_email',
            field=models.EmailField(max_length=254, verbose_name='E\\-mail do solicitante'),
        ),
    ]
