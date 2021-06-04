import pandas as pd
import numpy as np
import re


def read_df(path):
    return pd.read_csv(path)


def create_dataset_df(df):
    data = {'name': [], 'qualifiedName': [], 'path': [], 'mark': []}
    for index, row in df.iterrows():
        # =====================> Start transforming string representation of list to list
        source_datasets = eval(row['source_datasets'])
        target_datasets = eval(row['target_datasets'])
        # =====================> End transforming
        # Extracting other parameters
        path = "unknown"
        for source_dataset in source_datasets:
            # print(source_dataset)
            data['name'].append(source_dataset)
            data['qualifiedName'].append(source_dataset.replace(source_dataset.split('.')[0], '')[1:])
            data['path'].append(path)
            data['mark'].append('raw_dataset')
        for target_dataset in target_datasets:
            data['name'].append(target_dataset)
            data['qualifiedName'].append(target_dataset.replace(target_dataset.split('.')[0], '')[1:])
            data['path'].append(path)
            data['mark'].append('clean_dataset')

    return pd.DataFrame(data=data)


def export_df_to_csv(df, path):
    df.to_csv(path, index=False)


def main():
    df_1 = read_df('datalake-ped.csv')
    df_2 = read_df('datalake-cleansing.csv')
    df = pd.concat([df_1, df_2]).reset_index()
    export_df_to_csv(df, 'relations.csv')
    export_df_to_csv(create_dataset_df(df), 'datasets.csv')


if __name__ == "__main__":
    main()
