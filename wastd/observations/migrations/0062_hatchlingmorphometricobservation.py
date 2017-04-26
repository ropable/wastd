# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0061_turtlenestdisturbancetallyobservation_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='HatchlingMorphometricObservation',
            fields=[
                ('observation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='observations.Observation')),
                ('straight_carapace_length_mm', models.PositiveIntegerField(blank=True, help_text='The straight carapace length in millimetres.', null=True, verbose_name='Straight carapace length (mm)')),
                ('straight_carapace_width_mm', models.PositiveIntegerField(blank=True, help_text='The straight carapace width in millimetres.', null=True, verbose_name='Straight carapace width (mm)')),
                ('body_weight_g', models.PositiveIntegerField(blank=True, help_text='The body weight in grams (1000 g = 1kg).', null=True, verbose_name='Body weight (g)')),
            ],
            options={
                'abstract': False,
            },
            bases=('observations.observation',),
        ),
    ]