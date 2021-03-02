# AUTOGENERATED! DO NOT EDIT! File to edit: 02_metric.ipynb (unless otherwise specified).

__all__ = ['Metric']

# Cell
import json

# Cell
class Metric:
    "`Artemis API` Metric entity object"
    def __init__(self, client):
        self.client = client
        self.response = None

    def find_all(self, facility_id):
        "Retrieves all metrics for a specific facility"
        self.response = self.client.get(f'/facilities/{facility_id}/metrics')
        return self.response.json().get('data')

    def find(self, facility_id, metric_id):
        "Retrieves a specific metric for a specific facility"
        self.response = self.client.get(f'/facilities/{facility_id}/metrics/{metric_id}')
        return self.response.json().get('data')

    def create(self, facility_id, attributes):
        "Creates a new metric for a specific facility"
        data = {}
        body = {}
        data['type'] = "metrics"
        data['attributes'] = attributes
        body['facility_id'] = facility_id
        body['_jsonapi'] = {}
        body['_jsonapi']['data'] = data
        self.response = self.client.post(f'/facilities/{facility_id}/metrics', json.dumps(body))
        return self.response.json().get('data')