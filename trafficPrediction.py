import pandas as pd
import numpy as np
import os
import typing
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

path = "datasets"
ds = pd.DataFrame()
for file_name in os.listdir(path):
    temp = pd.read_csv(path + "//" + file_name, index_col='dateandtime',parse_dates=True)
    ds = ds.append(temp)

temp = pd.pivot_table(ds,index = 'dateandtime', values ='spdK/m' , columns ='edge')

temp = temp.groupby([
            pd.Grouper(level='dateandtime'
                       , freq = '7T'
                      )]
          ).mean()

limitPer = len(temp) * .90
df = temp.dropna(thresh=limitPer, axis=1)
df = df.fillna(temp.mean())
df = df.loc[:, (temp != 0).any(axis=0)]
#plt.plot(trainY)
plt.rcParams["figure.figsize"] = (30,15)
plt.plot(df.values[:,-1])
plt.plot(df.values[:,-2])
plt.show()