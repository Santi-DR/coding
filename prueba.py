import pandas as pd
import numpy as np

def my_function():
    pass

def get_data():
    data = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
    return data

get_data()
