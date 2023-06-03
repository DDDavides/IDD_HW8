import pandas as pd

"""Funzione che genera il dataframe di tutte le coppie di ennuple da etichettare

    choices = coppie di indici relativi alle ennuple da etichettare
    schema_cleaned = dataset pulito da cui prendere il contenuto delle ennuple relative a choices
    @return il dataframe delle coppie di ennuple da etichettare
"""
def get_datasetCouples_to_label(choices, schema_cleaned: pd.DataFrame):
    keys = schema_cleaned.columns
    lKeys = {key : f"l_{key}" for key in keys}
    rKeys = {key : f"r_{key}" for key in keys}

    idxKeys = ["id_1", "id_2"]

    choices_column = [*idxKeys, *lKeys.values(), *rKeys.values()] # id_1, id_2, l_attr, r_attr
    choices_df = pd.DataFrame(columns=choices_column) # 
    for choice in choices:
        lRow = schema_cleaned.iloc[[choice[0]]]
        rRow = schema_cleaned.iloc[[choice[1]]]

        lRow = lRow.rename(columns=lKeys).reset_index(drop=True)
        rRow = rRow.rename(columns=rKeys).reset_index(drop=True)

        idxs = pd.DataFrame({idxKeys[0]: [choice[0]], idxKeys[1]: [choice[1]]})
        row = pd.concat([idxs, lRow, rRow], axis=1)
        choices_df = pd.concat([choices_df, row], axis=0)

    # choices_df.reset_index(inplace=True)
    choices_df.set_index(idxKeys)
    return choices_df