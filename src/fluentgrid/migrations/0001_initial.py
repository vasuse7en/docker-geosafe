# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('geosafe', '0005_auto_20170914_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCCSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50, null=True, verbose_name=b'Name of CCC/System', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SimulationEventDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_response_id', models.TextField(default=b'', null=True, verbose_name=b'Response received from the upstream CCC/any other system', blank=True)),
                ('event_status', models.CharField(default=b'', max_length=30, null=True, verbose_name=b'Status of Event', blank=True)),
                ('analysis', models.ForeignKey(related_name='simulation_event', to='geosafe.Analysis')),
                ('ccc_system', models.ForeignKey(related_name='simulation_ccc_system', to='fluentgrid.CCCSystem')),
            ],
        ),
        migrations.CreateModel(
            name='SimulationEventStatusLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'time')),
                ('status', models.CharField(default=b'', max_length=30, null=True, verbose_name=b'Status of Event', blank=True)),
                ('message', models.TextField(default=b'', null=True, verbose_name=b'Message/detail about the status change', blank=True)),
                ('simulation_event_id', models.ForeignKey(to='fluentgrid.SimulationEventDetails')),
            ],
        ),
        migrations.CreateModel(
            name='SimulationEventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30, null=True, verbose_name=b'Name of Simulation Event', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='simulationeventdetails',
            name='simulation_event_type',
            field=models.ForeignKey(related_name='simulation_event_type', to='fluentgrid.SimulationEventType'),
        ),
    ]
