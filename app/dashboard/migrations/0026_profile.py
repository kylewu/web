# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-23 15:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_bounty_issue_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('handle', models.CharField(db_index=True, max_length=255)),
                ('last_sync_date', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
