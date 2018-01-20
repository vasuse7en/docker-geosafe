import logging
import json
import datetime
import requests
from django.http.response import HttpResponse
from geosafe.models import Analysis
from geonode.layers.models import Layer
from fluentgrid.models import SimulationEventDetails, SimulationEventType, CCCSystem
from fluentgrid.types.Constants import Certainty, Constant, Urgency
# from fluentgrid.integration.event.EventgeneratorFactory import EventFactory
# from fluentgrid.integration.event.Event import BaseEvent
LOGGER = logging.getLogger("geosafe")

logger = logging.getLogger("geonode.geosafe.analysis")


# Create your views here.
def send_event(request):
    try:
        analysis_id = request.POST.get("analysis_id", "")
        analysis = Analysis.objects.get(id=analysis_id)
        event_type = request.POST.get("type", "")
        system = request.POST.get("system", "")
        simulation_event_type = SimulationEventType.objects.filter(name=event_type)
        ccc_system = CCCSystem.objects.filter(name=system)

        detail = SimulationEventDetails(analysis=analysis, simulation_event_type=simulation_event_type[0],
                                        ccc_system=ccc_system[0], event_status='NEW')
        detail.save()
        # id = detail.id
        # BaseEvent = EventFactory.getEventgenerator(detail.ccc_system)
        # BaseEvent.generate();



        lat_lon = detail.analysis.user_extent.split(",")
        lon = (float(lat_lon[0]) + float(lat_lon[2])) / 2
        lat = (float(lat_lon[1]) + float(lat_lon[3])) / 2
        alert_name = Layer.objects.get(id=detail.analysis.impact_layer_id).title
        data = {}
        data['apikey'] = Constant.FG_CCC_REST_END_POINT
        data['Source'] = 'Fluentgrid Disaster Simulation'
        data['DeviceName'] = 'Disaster Simulation module'
        data['AlertName'] = alert_name
        # data['Description'] = detail.analysis.description TODO
        data['RaisedOn'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['Latitude'] = lat
        data['Longitude'] = lon
        # data['Location'] = TODO
        # data['MessageId'] = detail.id TODO
        # data['SenderId'] = detail.id TODO
        # data['SenderName'] = detail.id TODO
        # data['Urgency'] = detail.id TODO
        # data['Certainty'] = detail.id TODO
        # data['Contact'] = detail.id TODO
        # data['ResourceDesc'] = detail.id TODO
        # data['MimeType'] = detail.id TODO
        # data['Size'] = detail.id TODO
        # data['Uri'] = detail.id TODO
        # data['DerefUri'] = detail.id TODO
        # data['Polygon'] = detail.id TODO
        # data['Geocode'] = detail.id TODO

        json_data = json.dumps(data)

        # response = requests.post("https://10.10.39.113:8443/apiman-gateway/Fluentgrid/SimulationAPI/1.0", data=json_data,
        #                          auth=('VizagUser', 'vizAg@123'))

        # headers = {'content-type': 'application/json'}
        url = Constant.FG_CCC_REST_END_POINT
        params = {'apikey': Constant.FG_CCC_REST_END_POINT_API_KEY}
        response = requests.post(url, params=params, data=json_data,
                                 auth=(Constant.FG_CCC_REST_END_POINT_USER, Constant.FG_CCC_REST_END_POINT_PASS))
        print(response)

        return HttpResponse(json.dumps({
            'success': True
        }), content_type='application/json')
    except Exception as e:
        LOGGER.exception(e)
        return HttpResponse(json.dumps({
            'success': False
        }), content_type='application/json')
