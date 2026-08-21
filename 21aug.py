from importlib import machinery
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data={
    'Area':[1000,1200,1500,1800,2000,2200,2500,2800,3000,3200],
    'bedroom':[2,2,3,3,3,4,4,4,5,5],   
    'price':[50,55,65,75,80,90,100,110,120,130]  
}

df=pd.dataframe(data)
print("Dataset")
print(df)
X=df[['Area','bedroom']]
y=df['price']