# AUTOGENERATED! DO NOT EDIT! File to edit: 00_client.ipynb (unless otherwise specified).

__all__ = ['APIClient']

# Cell
import os
from requests_oauthlib import OAuth2Session

# Cell
class APIClient:
    "API Client that enables to authenticate and connect to the `Artemis API`. You need to create an instance of the client to be able to interact with the API"
    def __init__(self, token=None, auth_code=None,
                 redirect_uri=None, automatic_refresh=True):

        if (token is None) & (auth_code is None):
            raise ValueError('You must either provide your token or an authorization code.')

        self.app_id = os.environ['ARTEMIS_OAUTH_APP_ID']
        self.app_secret = os.environ['ARTEMIS_OAUTH_APP_SECRET']
        self.base_uri = os.environ['ARTEMIS_BASE_URI']
        self.authorization_base_url = f"{self.base_uri}/oauth/authorize"
        self.token_url = f"{self.base_uri}/oauth/token"
        self.refresh_url = self.token_url
        self.url_prefix = '/api/v3'
        self.automatic_refresh = automatic_refresh
        if auth_code is not None:
            self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob' if redirect_uri is None else redirect_uri
            self.oauth_client = OAuth2Session(self.app_id, redirect_uri=self.redirect_uri)
            authorization_response = f"{self.base_uri}/oauth/authorize/native?code={auth_code}"
            self.token = self.oauth_client.fetch_token(
                self.token_url,
                authorization_response=authorization_response,
                client_secret=self.app_secret)
        else:
            self.oauth_client = OAuth2Session(self.app_id, token=token)
            self.token = self.update_token()

        self.update_client_information()

    def set_url(self, url):
        "Process a url and sets it accordingly for the API calls. The base_url and the url_prefix will be concatenated (preceed) the url"
        return f'{self.base_uri}{self.url_prefix}{url}'

    def get(self, url):
        "Performs a GET request for the url"
        headers = {"Content-Type": "application/json"}
        if self.automatic_refresh:
            self.token = self.update_token()
            self.update_client_information()
        return self.oauth_client.get(self.set_url(url), headers=headers)

    def post(self, url, data):
        "Performs a POST request for the url and parameters"
        headers = {"Content-Type": "application/json"}
        if self.automatic_refresh:
            self.token = self.update_token()
            self.update_client_information()
        return self.oauth_client.post(self.set_url(url), data=data, headers=headers)

    def put(self, url, data):
        "Performs a PUT request for the url and parameters"
        headers = {"Content-Type": "application/json"}
        if self.automatic_refresh:
            self.token = self.update_token()
            self.update_client_information()
        return self.oauth_client.put(self.set_url(url), data=data, headers=headers)

    def delete(self, url, data=None):
        "Performs a DELETE request for the url"
        headers = {"Content-Type": "application/json"}
        if self.automatic_refresh:
            self.token = self.update_token()
            self.update_client_information()
        if data is None:
            return self.oauth_client.delete(self.set_url(url), headers=headers)
        else:
            return self.oauth_client.delete(self.set_url(url), data=data, headers=headers)

    def update_token(self):
        "Refreshes the client's API token"
        return self.oauth_client.refresh_token(self.refresh_url, client_id=self.app_id, client_secret=self.app_secret)

    def update_client_information(self):
        "Update the client's token information"
        self.access_token = self.token.get('access_token')
        self.token_type = self.token.get('token_type')
        self.refresh_token = self.token.get('refresh_token')
        self.expires_at = self.token.get('expires_at')
        return None

    def response_handler(self, response, body=None):
        "Handles response depending on status code"
        if response.status_code == 200:
            return response.json().get('data')
        elif response.status_code == 204:
            return body
        else:
            try:
                response.json()['data']
            except:
                print(f"Request Failed - {response.status_code}: {response.reason}")
                return None
            return response.json().get('data')