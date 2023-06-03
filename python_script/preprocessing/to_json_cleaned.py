import os 
from cleanDataframe import *
from utility import *

path = "./datasets"
to_path = './json_datasets'
for dir in os.listdir(path):
    dirpath = f"{path}/{dir}"
    if os.path.isfile(dirpath):
        continue
    
    # trasforma e pulisce tutti i dataset salvandoli in formato json
    for file in os.listdir(dirpath):
        filepath = f"{dirpath}/{file}"
        filename = os.path.splitext(file)[0]
        path_to_save = f"{to_path}/{dir}-{filename}.json" 
        try:
            # prima pulisci il db e poi trasformalo in json
            fromDBpathToDataframeCleaned(filepath).to_json(path_to_save)
        except:
            print(filepath)