import requests
import json
from GetNameByGuid import get_guid_by_name, get_name_by_guid

url = "http://localhost:21000/api/atlas/v2/entity/guid/%s"

header = {"Content-Type": "application/json",
          "Accept": "application/json",
          "Cache-Control": "no-cache"}


def delete_by_name(name):
    """
    In this function we deleting entity by name firstly transform this name to guid sending DELETE request to Atlas REST API
    :param name:
    :return: status code of request. If status code is 200 thant entity was deleted
    """
    guid = get_guid_by_name(name)
    if guid is not None:
        x = requests.delete(url % get_guid_by_name(name), auth=('admin', 'admin'))
        if x.status_code == 200:
            print(f"Entity with guid {guid} was deleted.\n")
        else:
            print(f"Entity with guid {guid} was not deleted.\n")
        return x.status_code
    return 500


def delete_by_guid(guid):
    """
    In this function we deleting entity by guid sending DELETE request to Atlas REST API
    :param guid:
    :return:
    """
    if guid is not None:
        x = requests.delete(url % guid, auth=('admin', 'admin'))
        if x.status_code == 200:
            print(f"Entity with guid {guid} was deleted.\n")
        else:
            print(f"Entity with guid {guid} was not deleted.\n")
        return x.status_code
    return 500
