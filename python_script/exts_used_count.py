import os
import pandas as pd

def exts_count():
    exts_used = {}
    root = "../datasets"
    for dir in os.listdir(root):
        dir_path = f"{root}/{dir}"
        for file in os.listdir(dir_path):
            _, file_ext = os.path.splitext(file)
            if file_ext in exts_used.keys():
                exts_used[file_ext] += 1
            else: 
                exts_used[file_ext] = 1
    return(exts_used)