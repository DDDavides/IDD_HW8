import pandas as pd
import regex as re

# funzione che pulisce il dataframe pulito come segue:
#     (1) Elimina spazi superflui
#     (2) Elimina \n e \r
def cleanDataframeRows(df):
   numColumns = len(df.columns) # numero di colonne del dataset
   columnsName = df.columns     # colonne del dataset

   # modifico inplace ogni colonna di ogni riga
   for idx,_ in df.iterrows():
      for colIdx in range(numColumns):
         cellData = df.loc[idx, columnsName[colIdx]] # dato nella cella di una riga relativo ad una colonna
         try:
            cellData = re.sub(r'\n|\r',' ',cellData) # regex per (2)
            cellData = cellData.strip()             # (1)
            df.loc[idx, columnsName[colIdx]] = cellData # sostituzione inplace
         except:
            continue