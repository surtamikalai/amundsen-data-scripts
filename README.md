# Installation
```bash
cd your/path/to/amundsen
docker-compose -f docker-amundsen-atlas.yml up
```
# Run sample loader
```bash
    cd your/path/to/this/project
    python load_sample.py
```


# Web UI
After amundsen install for web UI open localhost:21000 with  login = admin and password = admin

# How apache atlas works
You are have typedefs, entities. Typedef it similary to programming languages and it somethink like class, here you should describe common parameters such as name of class
description of the typedef, some classification using which we can mark the typedef and after that you should to describe parameters of the typedef(look on typedef_datasets.json)

Entity it's like object of the class in programming languages. You can create essence of your typedef using CreateDatasetEntity.py


GetEntity.py should return entities guid. But now it returns guid of all entities of current typeName.

DeleteEntity.py delete entity by guid.

CreateTypedefs.py сreates typedef using the json file.

CreateDatasetEntity.py creates entity of dataset using next parameters: qualifiedName, name, path(path to dataset), classifications(raw_dataset or clean_dataset), 
col_schema(it's schema of columns of dataset)

CreateSparkProcessEntities.py creates entity that connect two datasets that you are give as a parameters: input_guid and output_guid.

# Plans
1. Automate creating spark process entities
2. Create json file for storing guid of each added dataset (Completed)
3. Make requests asyncronus

amundsen (can use Neo4j or Atlas as backbone)