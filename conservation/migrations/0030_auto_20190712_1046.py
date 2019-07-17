# Generated by Django 2.2.3 on 2019-07-12 02:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conservation', '0029_auto_20190712_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityconservationlisting',
            name='source_id',
            field=models.CharField(default=uuid.UUID('3e934371-a44f-11e9-84cb-9cb6d0bfcf25'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
        migrations.AlterField(
            model_name='conservationcategory',
            name='level',
            field=models.CharField(choices=[('extinct', 'Extinct'), ('collapsed', 'Collapsed'), ('threatened', 'Threatened'), ('specially-protected', 'Specially Protected'), ('other', 'Other'), ('priority', 'Priority')], db_index=True, default='other', help_text='A convenience grouping of several conservation levels for efficient filtering of records in TSC.', max_length=500, verbose_name='Filter group'),
        ),
        migrations.AlterField(
            model_name='conservationcategory',
            name='short_code',
            field=models.CharField(choices=[('X', 'Extinct'), ('CO', 'Collapsed'), ('T', 'Threatened'), ('SP', 'Specially Protected'), ('O', 'Other'), ('1', 'Priority 1'), ('2', 'Priority 2'), ('3', 'Priority 3'), ('4', 'Priority 4'), ('5', 'Priority 5')], db_index=True, default='O', help_text='A conservation code exported to FloraBase', max_length=500, verbose_name='FloraBase Code'),
        ),
        migrations.AlterField(
            model_name='taxonconservationlisting',
            name='source_id',
            field=models.CharField(default=uuid.UUID('3e934371-a44f-11e9-84cb-9cb6d0bfcf25'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
    ]