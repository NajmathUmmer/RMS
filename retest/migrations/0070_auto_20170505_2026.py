# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0069_retest_is_rep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retest',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
