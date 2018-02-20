from fluentgrid.types.Constants import IntegrationCCCSystem
import datetime
from geosafe.models import Metadata
import json
import requests
from fluentgrid.types.Constants import Certainty, Constant, Urgency
from geonode.layers.models import Layer
from django.core.urlresolvers import reverse
from django.http import HttpRequest
import unicodedata


def system_factory(system_name):
    if system_name == IntegrationCCCSystem.FG_CCC:
        system = FluentgridCCC
    elif system_name == IntegrationCCCSystem.IBM_IOC:
        system = IbmIOC
    else:
        raise ValueError('Cannot connect to {}'.format(system_name))
    return system()


def get_system(system):
    factory = None
    try:
        factory = system_factory(system)
    except ValueError as ve:
        print(ve)
    return factory


class FluentgridCCC:

    def send_event(self, detail, request):
        try:
            lat_lon = detail.analysis.user_extent.split(",")
            lon = (float(lat_lon[0]) + float(lat_lon[2])) / 2
            lat = (float(lat_lon[1]) + float(lat_lon[3])) / 2
            data = {}
            hazard_category = Metadata.objects.get(layer_id=detail.analysis.hazard_layer.id).category
            exposure_category = Metadata.objects.get(layer_id=detail.analysis.exposure_layer.id).category
            data['Source'] = 'DISSIM'
            # data['DeviceName'] = 'Fluentgrid ERM'
            data['AlertName'] = hazard_category.capitalize() + " Alert"
            data['Description'] = detail.event_description
            data['RaisedOn'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data['Latitude'] = lat
            data['Longitude'] = lon
            url = reverse('geosafe:download-report', kwargs={'analysis_id': detail.analysis.id, 'data_type': "map"})
            map_url = request.build_absolute_uri(url)
            url = reverse('geosafe:download-report', kwargs={'analysis_id': detail.analysis.id, 'data_type': "table"})
            table_url = request.build_absolute_uri(url)
            url = reverse('geosafe:download-report', kwargs={'analysis_id': detail.analysis.id, 'data_type': "all"})
            all_url = request.build_absolute_uri(url)
            url = reverse('geosafe:analysis-create', kwargs={'pk': detail.analysis.id})
            analysis_url = request.build_absolute_uri(url)
            resource_1 = {"ResourceDesc": "Map report", "MimeType": 'application/pdf', "Size": "", "Uri": map_url}
            resource_2 = {"ResourceDesc": "Table report", "MimeType": 'application/pdf', "Size": "", "Uri": table_url}
            resource_3 = {"ResourceDesc": "GIS and impact report data", "MimeType": 'application/zip', "Size": "",
                          "Uri": all_url}
            resource_4 = {"ResourceDesc": "Simulation Url", "MimeType": '', "Size": "", "Uri": analysis_url}
            resource = [resource_1, resource_2, resource_3, resource_4]

            data['Resource'] = resource
            data['Location'] = "Visakhapatnam CCC Data Center"
            data['MessageId'] = detail.id
            data['SenderId'] = "disaster_simulation@fluentgrid.ccc"
            data['SenderName'] = "Disaster Simulation"
            data['Urgency'] = detail.urgency
            data['Certainty'] = detail.certainty
            # data['Contact'] = detail.id TODO
            # data['Polygon'] = detail.id TODO
            # data['Geocode'] = detail.id TODO

            json_data = json.dumps(data)
            json_data = 'data=[' + json_data + ']'
            print(json_data)
            url = Constant.FG_CCC_REST_END_POINT
            access_token = self.get_access_token()
            access_token = unicodedata.normalize('NFKD', access_token).encode('ascii', 'ignore')
            print access_token
            params = {'apikey': Constant.FG_CCC_REST_END_POINT_API_KEY}
            response = requests.post(url,
                                     params=params, headers={'Authorization': 'bearer %s' % access_token},
                                     data=json_data, verify=False)
            return response
        except Exception as e:
            raise ValueError(e.message)

    def get_access_token(self):
        url = Constant.FG_CCC_SSO_END_POINT
        password = Constant.FG_CCC_SSO_END_POINT_PASS
        user = Constant.FG_CCC_SSO_END_POINT_USER

        data = {'username': user, 'password': password, 'grant_type': 'password', 'client_id': 'Simulation'}
        response = requests.post(url, data=data, verify=False)
        result = ""
        if response.status_code == 200:
            json_data = json.loads(response.text)
            result = json_data['access_token']
        elif response.status_code == 404:
            raise ValueError("The CCC/System you chose is not running at the moment")
        elif response.status_code == 401:
            raise ValueError("Unauthorized")
        else:
            raise ValueError("Cannot authenticate with CCC")
        return result


class IbmIOC:
    def send_event(self, detail, request):
        print("implementation not available")
        raise ValueError('Integration to IBM IOC is not yet implemented')
