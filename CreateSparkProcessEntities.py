import requests
import json

url = "http://localhost:21000/api/atlas/v2/entity/bulk"


def create_process(input_guid, output_guid, path, name):
    """
    In this function we creating relation between 2 entities changing basic dictionary and sending this dictionary to Atlas API
    :param name:
    :param path:
    :param input_guid: guid of input dataset or other entity
    :param output_guid:guid of input dataset or other entity
    :return: status code of request. If request completed successfully than it returns 200
    """
    data = {"entities": [
        {
            "typeName": "spark_process",
            "createdBy": "John Doe",
            "attributes": {
                "qualifiedName": "Cleansing",
                "name": "Cleansing",
                "description": "Clean data from raw to clean",
                "owner": "John Doe",
                "path": "my/path",
                "inputs": [{"guid": "1a3a8057-96fa-40bf-a386-c70db115ea1b",
                            "typeName": "data_object"}],
                "outputs": [{'guid': '1788268e-e104-4d12-a4b1-1aeff7c738b0', "typeName": "data_object"}]
            }
        }
    ]
    }
    data["entities"][0]["attributes"]["inputs"][0]["guid"] = input_guid
    data["entities"][0]["attributes"]["outputs"][0]["guid"] = output_guid
    data["entities"][0]["attributes"]["path"] = path
    data["entities"][0]["attributes"]["name"] = name
    data["entities"][0]["attributes"]["qualifiedName"] = name
    header = {"Content-type": "application/json",
              "Accept": "application/json",
              "Cache-Control": "no-cache"}
    # print(data)
    response_decoded_json = requests.post(url, json=data, headers=header, auth=('admin', 'admin'))
    return response_decoded_json.status_code
