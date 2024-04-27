# Package Imports 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import tensorflow as tf 
import matplotlib.pyplot as plt 

# Modelling Class Functionality 

class model: 
    def __init__(self, data):
        self.data = data 


    def linear_regression(self):
        