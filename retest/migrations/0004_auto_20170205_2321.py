# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0003_auto_20170205_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=50)),
                ('proof', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('admnno', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=1)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Departement')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Semester')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Student'),
        ),
        migrations.AddField(
            model_name='request',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Departement'),
        ),
        migrations.AddField(
            model_name='request',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Semester'),
        ),
        migrations.AddField(
            model_name='request',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Subject'),
        ),
    ]
