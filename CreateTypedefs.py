import requests
import json

url = "http://localhost:21000/api/atlas/v2/types/typedefs"

header = {"Content-Type": "application/json",
          "Accept": "application/json",
          "Cache-Control": "no-cache"}


def send_typedef(path_to_typedef_json):
    """Creates typedef using the json file passed in parameters
    :param path_to_typedef_json
        Path to json with definition of type
    :return status code of request if 200 than request are good
    """
    with open(path_to_typedef_json, "r") as json_file:
        payload = json.load(json_file)

    response_decoded_json = requests.post(url=url, json=payload, headers=header, auth=('admin', 'admin'))
    return response_decoded_json.status_code

# send_typedef("jsons/typedef_datasets.json")  # creates dataset typedef
