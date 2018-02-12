# from django import forms
# from django.forms import models
# from fluentgrid.models import SimulationEventDetails, SimulationEventType, CCCSystem
#
#
# class SendEventForm(forms.Form):
#     """A form for creating an event."""
#
#     simulation_event_type = forms.ModelChoiceField(
#         label='Event Type',
#         required=True,
#         queryset=SimulationEventType.objects.all(),
#     )
#
#     ccc_system = forms.ModelChoiceField(
#         label='CCC/System',
#         required=True,
#         queryset=CCCSystem.objects.all(),
#     )
