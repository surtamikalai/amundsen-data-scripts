import requests
import json
from GetGuid import get_entities
from GetNameByGuid import get_name_by_guid

url = "http://localhost:21000/api/atlas/v2/entity/bulk"


def create_dataset(qualified_name, name, path, classifications, col_schema=[
    {"col": "id", "data_type": "string"},
    {"col": "scrap_time", "data_type": "timestamp"},
    {"col": "url", "data_type": "string"},
    {"col": "headline", "data_type": "string"},
    {"col": "content", "data_type": "string"}
]):
    """
    In this function we create dataset changing basic dictionary and sending this dictionary to Atlas API
    :param qualified_name: Parameter of dataset, should be unique
    :param name: Name of dataset that we can see in UI
    :param path: Path to dataset
    :param classifications: If it's raw dataset we should mark it like raw_dataset, or if it's clean dataset we should mark it like clean_dataset
    :param col_schema: Schema of dataset
    :return: status code of request. If request completed successfully than it returns 200
    """
    # dictionary that we will send with POST request, here we should define our entity
    data = {
        "entities": [
            {
                "typeName": "data_object",
                "createdBy": "John Doe",
                "attributes": {
                    "description": "Dataset object",
                    "qualifiedName": "manual_driveTime",
                    "name": "manual.driveTime",
                    "path": "https://bitbucket.org/emea_cf/datalake-cleansing/src/master/datalake-cleansing-jobs/src/main/scala/com/goodyear/datalake/cleansing/current/jobs/external/aligneddistribution/carage/CarAgeTask.scala",
                    "frequency": "1",
                    "owner": "John Doe",
                    "group": "GoodYear",
                    "format": "nc",
                    "col_schema": [
                        {"col": "id", "data_type": "string"},
                        {"col": "scrap_time", "data_type": "timestamp"},
                        {"col": "url", "data_type": "string"},
                        {"col": "headline", "data_type": "string"},
                        {"col": "content", "data_type": "string"}
                    ]
                },
                "classifications": [
                    {"typeName": "raw_dataset"}
                ]
            }
        ]
    }

    # ====================> Changing keys of basic dictionary to custom
    data["entities"][0]["attributes"]["qualifiedName"] = qualified_name
    data["entities"][0]["attributes"]["name"] = name
    data["entities"][0]["attributes"]["path"] = path
    data["entities"][0]["classifications"][0]["typeName"] = classifications
    data["entities"][0]["attributes"]["col_schema"] = col_schema
    # =====================> End of changing
    header = {"Content-type": "application/json",
              "Accept": "application/json",
              "Cache-Control": "no-cache"}
    try:
        response_decoded_json = requests.post(url, json=data, headers=header, auth=('admin', 'admin'))
    except:  # If we can't send POST request than nothing to do 😥
        print("Can't send POST request")
    if response_decoded_json.status_code == 200:
        # if successful load than add new guid to json file
        new_dataset_guid()
    return response_decoded_json.status_code


def new_dataset_guid():
    """
    In this function we adding to our local file name and guid of dataset that was added to the server
    :Algorithm
        1. Getting all guids from our local file
        2. Getting all guid from Atlas server
        3. Finding difference between this sets of guids
        4. Adding guid that have Atlas server but local file have not
        5. Saving local file with new added guid
    :return: None
    """
    d = dict()
    with open('datasets_guid.json') as json_file:
        d = json.loads(json_file.read())
    guids = set(d.values())  # getting all guids of all created before entities
    try:
        old_with_one_new = get_entities({'type': 'data_object'})  # getting all guid from server
        try:
            # if this guid is not exists in json file than it's new guid add this as a new item in json
            new_guid = next(iter(set(old_with_one_new).difference(guids)))
        except StopIteration:  # if we meet StopIteration than we have no new guid it means that we added the same name
            print("No new entities are created!")
        else:
            try:
                entity_name = get_name_by_guid(new_guid)  # getting name of entity by guid
            except ConnectionRefusedError as e:  # If our request isn't work
                print(e)
            else:
                d[entity_name] = new_guid
                with open("datasets_guid.json", "w") as json_file:
                    json_file.write(json.dumps(d))
    except KeyError:  # If we haven't entities in json
        print("There no entities now!")


if __name__ == "__main__":
    print(create_dataset("new_name", "new_name", "zxc/path", "raw_dataset"))
