import requests
import json

url = "http://localhost:21000/api/atlas/v2/entity/guid/"


def get_name_by_guid(guid):
    """In this function we getting name of entity by using request to Atlas API.
    :param guid
        This parameter mean unique id of entity in Atlas database
    :return name
        name of guid
    :raise ConnectionRefusedError
        When we can't to make GET request or entity with this guid is not exists we will raise ConnectionRefusedError
    """
    response_decoded_json = requests.get(url=url + guid, auth=('admin', 'admin'))
    if response_decoded_json.status_code == 200:
        return response_decoded_json.json()['entity']['attributes']['name']
    else:
        raise ConnectionRefusedError("Can't make request!")


def get_guid_by_name(name):
    """
    :param name:
    :return: None if we haven't entity with this name
             guid of entity
    """
    res = None
    with open('datasets_guid.json') as json_file:
        res = json.loads(json_file.read()).get(name)
    return res


if __name__ == "__main__":
    print(get_guid_by_name("zxc.zc"))
