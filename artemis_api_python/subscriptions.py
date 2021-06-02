# AUTOGENERATED! DO NOT EDIT! File to edit: 09_subscriptions.ipynb (unless otherwise specified).

__all__ = ['Subscriptions']

# Cell
import json

# Cell
class Subscriptions:
    "`Artemis API` (notifications) Subscriptions entity object"
    def __init__(self, client):
        self.client = client
        self.response = None

    def find(self, subscription_id):
        "Retrieves a specific notification subscription"
        self.response = self.client.get(f'/subscriptions/{subscription_id}')
        return self.client.response_handler(self.response)

    def find_all(self):
        "Retrieves a list of notification subscriptions for the current user and OAuth application"
        self.response = self.client.get(f'/subscriptions')
        return self.client.response_handler(self.response)

    def create(self, attributes):
        "Creates a new notification subscription"
        data = {}
        body = {}
        data['type'] = "subscriptions"
        data['attributes'] = attributes
        body['_jsonapi'] = {}
        body['_jsonapi']['data'] = data
        self.response = self.client.post(f'/subscriptions', json.dumps(body))
        return self.client.response_handler(self.response, body)

    def remove(self, subscription_id):
        "Deletes a specific subscription"
        self.response = self.client.delete(f'/subscriptions/{subscription_id}')
        return self.client.response_handler(self.response)