from CreateTypedefs import send_typedef
from CreateDatasetEntity import create_dataset
from CreateSparkProcessEntities import create_process
from GetNameByGuid import get_guid_by_name
import pandas as pd

send_typedef("jsons/typedef_datasets.json")  # creating typedef dataset if it not exists


def create_entities(df):
    created = 0
    all = df.shape[0]
    for ind, row in df.iterrows():
        # print(row['qualifiedName'], row['name'], row['path'], row['mark'])
        if create_dataset(row['qualifiedName'], row['name'], row['path'], row['mark']) == 200:
            print(f"Dataset {row['name']} created")
            created += 1
        else:
            print(f"Dataset {row['name']} aborted")
    print(f"{created} / {all}")


def create_processes(df):
    created = 0
    all = df.shape[0]
    for index, row in df.iterrows():
        # =====================> Start transforming string representation of list to list
        source_datasets = eval(row['source_datasets'])
        target_datasets = eval(row['target_datasets'])
        # =====================> End transforming
        # Extracting other parameters
        path = row['location']
        task_name = row['task_name']

        for source_dataset in source_datasets:
            for target_dataset in target_datasets:
                if create_process(get_guid_by_name(source_dataset), get_guid_by_name(target_dataset), path,
                                  task_name) == 200:
                    print(f"Process with name {task_name} was created")
                    created += 1
                else:
                    print(f"Process with name {task_name} wasn't created")
        print(f"Created {created}/{all}")


if __name__ == "__main__":
    create_entities(pd.read_csv('datasets.csv'))
    create_processes(pd.read_csv('relations.csv'))
