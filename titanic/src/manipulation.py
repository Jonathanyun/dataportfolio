
# Package Imports 
import seaborn as sns 
import pandas as pd 
import numpy as np 

# Function for Feature Enginnering 
def titanic_manipulation(df):
    """ Function that manipulates the titanic data set"""

    if isinstance(df, pd.DataFrame):
        # Dropping the name columns
        df.drop(['Name', 'Ticket', 'Cabin'], axis = 1)

        # Start of Feature Engineering dataset variables
        one_hot_encoded_data = pd.get_dummies(df, columns = ['Pclass', 'Sex', 'Embarked'])
        df_encoded = pd.concat([df, one_hot_encoded_data], axis = 1)
        df_encoded = df_encoded.drop(['Pclass', 'Sex', 'Embarked', 'Name', 'Ticket', 'Cabin'], axis = 1)

        return df_encoded
    else:
        return "Object is not a Pandas DataFrame"



