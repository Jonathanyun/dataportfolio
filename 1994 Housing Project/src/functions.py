import pandas as pd 
import numpy as np 



def load_data(): 
    """ 
    Loading in the housing data
    """

    data = pd.read_csv('../data/housing.csv')

    return data 
