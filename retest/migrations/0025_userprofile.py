# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 06:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retest', '0024_auto_20170326_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, max_length=255, null=True, upload_to=('main.UserProfile.photo', 'profiles'), verbose_name='Profile Picture')),
                ('Departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Departement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
