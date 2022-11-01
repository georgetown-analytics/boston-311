#####################################################################
# This file merges the 311 and weather data
#####################################################################
import matplotlib.pyplot as plt
from datetime import date
import seaborn as sns
import numpy as np

# run 311 import file
%run -t import-311-data.py

# run rainfall import file
%run -t import-weather-data.py

# convert the closed date to a date time format
df_311['closed_dt'] = pd.to_datetime(df_311['closed_dt'])

df_311['open_dt'] = pd.to_datetime(df_311['open_dt'])

# convert date to simple data not date time and rename for merge

df_311['date'] = pd.to_datetime(df_311['open_dt']).dt.normalize()

# merge

df_311_rainfall = pd.merge(df_311, df_prcp, how = 'left', on='date')


