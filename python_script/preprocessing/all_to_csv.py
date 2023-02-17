import os 
from cleanDataframe import *
from utility import *

path = "./datasets"
csv_path = './csv_datasets'
for dir in os.listdir(path):
    dirpath = f"{path}/{dir}"
    if os.path.isfile(dirpath):
        continue
    
    # trasforma tutti i dataset in formato csv senza pulirli
    for file in os.listdir(dirpath):
        filepath = f"{dirpath}/{file}"
        filename = os.path.splitext(file)[0]
        path_to_save = f"{csv_path}/{dir}-{filename}.csv" 
        try:
            # db trasformato in csv senza pulirlo
            fromDBpathToDataframe(filepath).to_csv(path_to_save)
        except:
            print(filepath)