# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('retest', '0039_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
