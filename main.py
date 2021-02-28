import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# load dataset
dataset = pd.read_csv('data/Google_Stock_Price_Train.csv', index_col='Date', parse_dates=True)

# convert data-types in dataset
dataset['Close'] = dataset['Close'].str.replace(',','').astype(float)
dataset['Volume'] = dataset['Volume'].str.replace(',','').astype(float)