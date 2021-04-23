# AUTOGENERATED! DO NOT EDIT! File to edit: 04_data_requests.ipynb (unless otherwise specified).

__all__ = ['DataRequests']

# Cell
import json

# Cell
class DataRequests:
    "`Artemis API` Data Requests entity object"
    def __init__(self, client):
        self.client = client
        self.response = None

    def create(self, facility_id, sensor_id, metric_id, attributes):
        "Creates a data request for a specific facility"
        data = {}
        body = {}
        data['type'] = "data_requests"
        data['attributes'] = attributes
        body['facility_id'] = facility_id
        body['_jsonapi'] = {}
        body['_jsonapi']['data'] = data
        self.response = self.client.post(f'/facilities/{facility_id}/data_requests', json.dumps(body))
        return self.client.response_handler(self.response, body)