# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluentgrid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationeventdetails',
            name='certainty',
            field=models.CharField(default=b'', max_length=30, null=True, verbose_name=b'Defined Certainty', blank=True),
        ),
        migrations.AddField(
            model_name='simulationeventdetails',
            name='event_description',
            field=models.TextField(default=b'', null=True, verbose_name=b'Description about the event', blank=True),
        ),
        migrations.AddField(
            model_name='simulationeventdetails',
            name='urgency',
            field=models.CharField(default=b'', max_length=30, null=True, verbose_name=b'Defined Urgency', blank=True),
        ),
    ]
