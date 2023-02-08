from valentine import valentine_match
from valentine.algorithms import Coma
from valentine.algorithms import Cupid
from valentine.algorithms import DistributionBased
from valentine.algorithms import JaccardLevenMatcher
from valentine.algorithms import SimilarityFlooding

# Metodi per il calcolo del match tra le colonne dei dataset passati nella tupla
# @param tupla = (nome dataset1, nome dataset2, dataframe1, dataframe2)
# @return nome dataset1, nome dataset2, il valore del matching di valentine

# COMA schema-based
def calculate_match_coma_schema(tupla):
    matcher = Coma(strategy="COMA_OPT")
    return tupla[0], tupla[1], valentine_match(tupla[2], tupla[3], matcher)

# CUPID (schema-based)
def calculate_match_cupid(tupla):
    matcher = Cupid()
    return tupla[0], tupla[1], valentine_match(tupla[2], tupla[3], matcher)

# SimilarityFlooding (schema-based)
def calculate_match_sim(tupla):
    matcher = SimilarityFlooding()
    return tupla[0], tupla[1], valentine_match(tupla[2], tupla[3], matcher)

# COMA instance-based
def calculate_match_coma_instance(tupla):
    matcher = Coma(strategy="COMA_OPT_INST")
    return tupla[0], tupla[1], valentine_match(tupla[2], tupla[3], matcher)

# Distribution-based (instance-based)
def calculate_match_distribution(tupla):
    matcher = DistributionBased()
    return tupla[0], tupla[1], valentine_match(tupla[2], tupla[3], matcher)

# Jaccard (instance-based)
def calculate_match_jaccard(tupla):
    matcher = JaccardLevenMatcher()
    return tupla[0], tupla[1], valentine_match(tupla[2], tupla[3], matcher)