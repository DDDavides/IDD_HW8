import os

# Funzione che calcola, data una cartella, quali tipi di file (che sono dentro la cartella) sono stati usati e quante volte
def exts_count(rootDirPath):
    # Dizionario Key=Estensione Value=Numero di volte che l'estensione relativa è usata
    exts_used = {}
    # Itero per tutte le cartelle dentro quella cui path è il parametro
    for dir in os.listdir(rootDirPath):
        dir_path = f"{rootDirPath}/{dir}"
        # Se è una cartella allora devo visitare i file al suo interno
        if os.path.isdir(dir_path):
            for file in os.listdir(dir_path):
                # funzione che riporta il nomde del file e l'estensione
                _, sub_file_ext = os.path.splitext(file)
                # Controllo per vedere se l'estensione è stata già usata o no (i.e. update del value o inserimento nuova chiave)
                if sub_file_ext in exts_used.keys():
                    exts_used[sub_file_ext] += 1
                else: 
                    exts_used[sub_file_ext] = 1
    return(exts_used)