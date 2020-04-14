import pandas as pd

bills_per_pound = 453
pile_path = 'data/pile_of_money.csv'

def read_pile():
    return(pd.read_csv(pile_path))
