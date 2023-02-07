from valentine import valentine_match
from valentine.algorithms import Coma
from valentine.algorithms import Cupid

def calculate_match(tupla):
    matcher = Coma(strategy="COMA_OPT_INST")
    return tupla[0], tupla[1], valentine_match(tupla[2], tupla[3], matcher)