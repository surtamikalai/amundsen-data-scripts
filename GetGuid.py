import requests
import json
from urllib.parse import urlencode


def get_entities(params: dict):
    """
    In this function we getting all entities of that corresponds to params dictionary sending GET request to Altas REST API
    :param params: example of params dictionary {'type': 'data_object'}. For correct work we can only define :key: 'type'
    :return:
    :raise: raises KeyError when we haven't entities on Atlas Server
    """
    url = f'http://localhost:21000/api/atlas/entities?{urlencode(params, doseq=True)}'  # transforming params dictionary to url format
    # print(url)
    response_decoded_json = requests.get(url=url, auth=('admin', 'admin'))
    try:
        return response_decoded_json.json()['results']
    except KeyError as e:
        raise

# print(get_entity({'type': 'data_object'}))
