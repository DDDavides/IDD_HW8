import os 
# import pandas as pd

def to_json(filepath):
    extension = filepath.split(".")[-1]
    print(extension)

path = "./datasets"
for dir in os.listdir(path):
    dirpath = f"{path}/{dir}"
    
    if os.path.isfile(dirpath):
        continue

    for file in os.listdir(dirpath):
        filepath = f"{dirpath}/{file}"
        to_json(filepath)