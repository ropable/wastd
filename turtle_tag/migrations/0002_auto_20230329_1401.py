# Generated by Django 3.2.18 on 2023-03-29 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turtle_tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turtleobservation',
            options={'ordering': ('observation_datetime',)},
        ),
        migrations.AlterModelOptions(
            name='turtlespecies',
            options={'ordering': ('common_name',), 'verbose_name_plural': 'turtle species'},
        ),
        migrations.AddField(
            model_name='turtle',
            name='entered_by_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entered_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turtle',
            name='date_entered',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='turtle',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Indeterminate')], max_length=1),
        ),
    ]