# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0049_auto_20170430_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventauditorium',
            old_name='fromt',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='eventauditorium',
            old_name='to',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='eventclassroom',
            old_name='fromt',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='eventclassroom',
            old_name='to',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='eventextensioncable',
            old_name='fromt',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='eventextensioncable',
            old_name='to',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='eventlab',
            old_name='fromt',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='eventlab',
            old_name='to',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='eventmikesystem',
            old_name='fromt',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='eventmikesystem',
            old_name='to',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='eventprojector',
            old_name='fromt',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='eventprojector',
            old_name='to',
            new_name='start',
        ),
    ]
