from django.db import models
from datetime import datetime
from geosafe.models import Analysis


class SimulationEventType(models.Model):
    name = models.CharField(
        verbose_name='Name of Simulation Event',
        max_length=30,
        blank=True,
        null=True,
        default=''
    )


class CCCSystem(models.Model):
    name = models.CharField(
        verbose_name='Name of CCC/System',
        max_length=50,
        blank=True,
        null=True,
        default=''
    )


class SimulationEventDetails(models.Model):
    analysis = models.ForeignKey(
        Analysis, related_name='simulation_event')
    simulation_event_type = models.ForeignKey(
        SimulationEventType, related_name='simulation_event_type')
    ccc_system = models.ForeignKey(
        CCCSystem, related_name='simulation_ccc_system')
    event_response_id = models.TextField(
        verbose_name='Response received from the upstream CCC/any other system',
        blank=True,
        null=True,
        default=''
    )
    event_status = models.CharField(
        verbose_name='Status of Event',
        max_length=30,
        blank=True,
        null=True,
        default=''
    )


class SimulationEventStatusLog(models.Model):
    simulation_event_id = models.ForeignKey(SimulationEventDetails, on_delete=models.CASCADE)
    time = models.DateTimeField(
        'time',
        default=datetime.now
    )
    status = models.CharField(
        verbose_name='Status of Event',
        max_length=30,
        blank=True,
        null=True,
        default=''
    )
    message = models.TextField(
        verbose_name='Message/detail about the status change',
        blank=True,
        null=True,
        default=''
    )