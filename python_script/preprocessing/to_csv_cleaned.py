import os 
from cleanDataframe import *
from utility import *

path = "./datasets"
csv_path = './csv_datasets_cleaned'
for dir in os.listdir(path):
    dirpath = f"{path}/{dir}"
    if os.path.isfile(dirpath):
        continue
    
    # trasforma e pulisce tutti i dataset salvandoli in formato csv
    for file in os.listdir(dirpath):
        filepath = f"{dirpath}/{file}"
        filename = os.path.splitext(file)[0]
        path_to_save = f"{csv_path}/{dir}-{filename}.csv" 
        try:
            # prima pulisci il db e poi trasformalo in csv
            fromDBpathToDataframeCleaned(filepath).to_csv(path_to_save)
        except:
            print(filepath)