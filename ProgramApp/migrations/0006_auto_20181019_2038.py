# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-19 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProgramApp', '0005_auto_20181019_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program_registration',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProgramApp.program_update'),
        ),
    ]