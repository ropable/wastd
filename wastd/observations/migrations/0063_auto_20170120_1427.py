# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0062_hatchlingmorphometricobservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turtlemorphometricobservation',
            old_name='body_weight_mm',
            new_name='body_weight_g',
        ),
    ]