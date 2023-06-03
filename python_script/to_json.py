import os 
import pandas as pd
import json

def read_jsonl(filepath):
    with open(filepath, 'r') as json_file:
        json_list = list(json_file)

    result = []
    for json_str in json_list:
        result.append(json.loads(json_str))
    return result

def to_json(filepath):
    extension = os.path.splitext(filepath)[1]
    df = None

    if extension == '.xls' or extension == '.xlsx':
        df = pd.read_excel(filepath)
    elif extension == '.csv':
        try:
            df = pd.read_csv(filepath)
            df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
        except Exception as e:
            print(e)
    elif extension == '.jsonl':
        df = pd.DataFrame(read_jsonl(filepath))
    elif extension == '.json':
        df = pd.read_json(filepath)
    return df

path = "./datasets"
to_path = './json_datasets'
csv_path = './csv_datasets'
for dir in os.listdir(path):
    dirpath = f"{path}/{dir}"
    if os.path.isfile(dirpath):
        continue

    for file in os.listdir(dirpath):
        filepath = f"{dirpath}/{file}"
        filename = os.path.splitext(file)[0]
        path_to_save = f"{to_path}/{dir}-{filename}.json" 
        try:
            to_json(filepath).to_json(path_to_save)
        except:
            print(filepath)