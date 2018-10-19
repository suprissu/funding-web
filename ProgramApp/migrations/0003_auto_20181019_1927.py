# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-19 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProgramApp', '0002_program_registration_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program_registration',
            name='program',
        ),
        migrations.AddField(
            model_name='program_registration',
            name='test',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ProgramApp.program_registration'),
            preserve_default=False,
        ),
    ]
