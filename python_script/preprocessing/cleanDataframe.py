import pandas as pd

# funzione che pulisce il dataframe come segue:
#     1. Elimina spazi superflui
#     2. Elimina \n
def cleanDataframeRows(df):
   numColumns = len(df.columns)
   columnsName = df.columns
   # modifico inplace ogni colonna di ogni riga con il modulo ftfy
   for idx,_ in df.iterrows():
      for colIdx in range(numColumns):
         cellData = df.loc[idx, columnsName[colIdx]]
         try:
            cellData = cellData.replace(r'\n', '').strip()
            df.loc[idx, columnsName[colIdx]] = cellData
         except:
            continue