import os
import pandas as pd

exts_used = {}
root = "./datasets"
for dir in os.listdir(root):
    dir_path = f"{root}/{dir}"
    for file in os.listdir(dir_path):
        filename, file_ext = os.path.splitext(file)
        filename = filename.strip()
        file_ext = file_ext.strip()
        if file_ext == '':
            print("Ext empty for file: ", filename)
        if file_ext in exts_used.keys():
            exts_used[file_ext] += 1
        else: 
            exts_used[file_ext] = 1
print(exts_used)