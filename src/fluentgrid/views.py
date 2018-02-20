import logging
import json
from django.http.response import HttpResponse, HttpResponseServerError
from geosafe.models import Analysis, Metadata
from fluentgrid.types.Constants import Certainty, Urgency
from fluentgrid.models import SimulationEventDetails, SimulationEventType, CCCSystem
from fluentgrid.integration.integration import get_system
from django.shortcuts import render

LOGGER = logging.getLogger("geosafe")

logger = logging.getLogger("geonode.geosafe.analysis")


# Create your views here.
def send_event(request):
    try:
        analysis_id = request.POST.get("analysis_id", "")
        analysis = Analysis.objects.get(id=analysis_id)
        event_type = request.POST.get("type", "")
        system = request.POST.get("system", "")
        urgency = request.POST.get("urgency", "")
        certainty = request.POST.get("certainty", "")
        # hazard_category = Metadata.objects.filter(layer_id = analysis.hazard_layer.id).category

        # category  = hazard_category.category
        event_description = request.POST.get("event_description", "")
        simulation_event_type = SimulationEventType.objects.filter(name=event_type)
        ccc_system = CCCSystem.objects.filter(name=system)

        detail = SimulationEventDetails(analysis=analysis, simulation_event_type=simulation_event_type[0],
                                        ccc_system=ccc_system[0], event_status='NEW',
                                        event_description=event_description, urgency=urgency, certainty=certainty)
        detail.save()
        system_factory = get_system(system)
        response = system_factory.send_event(detail, request)
        if response.status_code == 200:
            # TODO and response.text == 'success', HANDLE ERRORS IN SUCCESS RESPONSE
            return HttpResponse(json.dumps({
                'success': True,
                'text': "Event sent to respective CCC/System"
            }), content_type='application/json')
        else:
            raise ValueError(response.text)
        # TODO send e.message if it is json serializable only
    except Exception as e:
        LOGGER.exception(e)
        return HttpResponseServerError(json.dumps({
            'success': False,
            'response': "Event sending falied"
        }), content_type='application/json')


def event_view(request, pk):
    event_types = SimulationEventType.objects.all()
    ccc_systems = CCCSystem.objects.all()
    certainty = Certainty()
    urgency = Urgency()
    certainty_members = [attr for attr in dir(certainty) if
                         not callable(getattr(certainty, attr)) and not attr.startswith("__")]
    urgency_members = [attr for attr in dir(urgency) if
                       not callable(getattr(urgency, attr)) and not attr.startswith("__")]
    ctx = {'event_types': event_types,
           'ccc_systems': ccc_systems,
           'analysis_id': pk,
           'certainty_members': certainty_members,
           'urgency_members': urgency_members,
           'success': False}
    template = 'send_event.html'
    return render(request, template, ctx)


def update_event_context(request):
    analysis_id = request.POST.get("analysis_id", "")
    response = request.POST.get("response", "")
    ctx = {
        'analysis_id': analysis_id,
        'Message': response
    }
    template = 'send_event.html'
    return render(request, template, ctx)
