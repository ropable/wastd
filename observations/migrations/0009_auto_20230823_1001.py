# Generated by Django 3.2.20 on 2023-08-23 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0008_auto_20230809_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encounter',
            name='as_latex',
        ),
    ]