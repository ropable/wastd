# Generated by Django 3.2.18 on 2023-03-31 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_tag', '0004_auto_20230331_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurtleTagObservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(blank=True, choices=[('L', 'Left'), ('R', 'Right')], max_length=1, null=True)),
                ('status', models.CharField(blank=True, choices=[('#', 'Query number - Tag on'), ('0L', 'False Id as Lost'), ('A1', 'Applied new - OK fix'), ('A2', 'No tag applied'), ('AE', 'Applied new - end clinch noted'), ('M', 'Missing - obs record'), ('M1', 'Missing  - NOT obs'), ('N', 'Not Recorded'), ('OO', 'Open at Obs - Tag came off & not refixed'), ('OX', 'Open at Obs - Tag refixed'), ('P', 'Present Obs - & Read only'), ('P_ED', 'Present Obs - nr F edge & Read'), ('P_OK', 'Present Obs - OK fix & Read'), ('PX', 'Present Obs - Tag#s not read'), ('Q', 'Query present'), ('R', 'Removed by Obs'), ('RC', 'Insecure at Obs - reclinched in situ'), ('RQ', 'Insecure at Obs - Action ??')], max_length=8, null=True)),
                ('position', models.SmallIntegerField(blank=True, null=True)),
                ('barnacles', models.BooleanField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('observation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tag_observations', to='turtle_tag.turtleobservation')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='observations', to='turtle_tag.turtletag')),
            ],
        ),
    ]