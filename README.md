# Artemis API
> This is a basic python wrapper for the Artemis API.


This file will become your README and also the index of your documentation.

## Install

`pip install artemis_api_python`

## How to use

You'll first need to create a client and authenticate to the API using OAuth2 and authentication code: 

### Using a generated authentication code to retrieve a token:

```python
client = APIClient(auth_code="0LOuiqULGUyEiZ_u7a9D7eUxYakwGHaYOUl3KvUtC14")
```

### By refreshing a token manually

```python
client_refresh = APIClient(token=client.token)
```
