# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0028_auto_20170326_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
