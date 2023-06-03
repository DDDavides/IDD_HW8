import pandas as pd
import os 
import json
from cleanDataframe import *

# legge jsonl riportando una lista di json object
def read_jsonl(filepath):
    with open(filepath, 'r') as json_file:
        json_list = list(json_file)

    result = []
    for json_str in json_list:
        result.append(json.loads(json_str))
    return result

# Questa funzione legge dataset da path e riporta il dataframe associato droppando la colonna unnamed se presente
# Formati accettati: .xls .xlsx .csv .jsonl .json
def fromDBpathToDataframe(filepath):
    extension = os.path.splitext(filepath)[1]
    df = None

    if extension == '.xls' or extension == '.xlsx':
        df = pd.read_excel(filepath)
    elif extension == '.csv':
        try:
            df = pd.read_csv(filepath, encoding='ISO-8859-1')
        except Exception as e:
            print(e)
    elif extension == '.jsonl':
        df = pd.DataFrame(read_jsonl(filepath))
    elif extension == '.json':
        df = pd.read_json(filepath)

    df.drop(df.filter(regex="Unnamed"),axis=1, inplace=True)
    return df

# legge il dataset da path e riporta il dataframe associato 
#       1. Senza l'eventuale colonna Unnamed 
#       2. Con pulizia dei dati (no spazi inutili, senza \n e \r)
# N.B. le estensioni permesse sono: .xls .xlsx .csv .jsonl .json
def fromDBpathToDataframeCleaned(filepath):
    df = fromDBpathToDataframe(filepath)
    cleanDataframeRows(df)
    return df