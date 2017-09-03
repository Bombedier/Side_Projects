import sklearn
import numpy as np
import pandas as pd
import statsmodels.api as sm
from arch import arch_model
import numba as nb
import matplotlib.pyplot as plt 

# import data into a pandas dataframe
# test for stationarity - augmented dickey-fuller test -> sm.tsa.adfuller()
# regress
# test with arch

data1 = pd.read_excel('pdstest.xlsx', 'CDS_Spread')
#df1 = 
# data2 = pd.read_xls('pdstest.xlsx')
