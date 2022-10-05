# This file imports data from noaa
# code is largely sources from this post: https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859

#needed to make web requests
import requests

#store the data we get as a dataframe
import pandas as pd

#convert the response as a strcuctured json
import json

#mathematical operations on lists
import numpy as np

#parse the datetimes we get from NOAA
from datetime import datetime

#add the access token you got from NOAA
# you will need to create a CSV file that has one column with the header, token, and then below that
# your token from NOAA
Token = pd.read_csv('/Users/jacobpstein/Desktop/weather_token.csv').iloc[0,0]

# Boston Airport station
station_id = 'GHCND:USW00014739'

#initialize lists to store data
dates_prcp = []
prcp = []


for year in range(2010, 2023):
    year = str(year)

    #make the api call
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=PRCP&limit=1000&stationid=GHCND:USW00014739&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
    #load the api response as a json
    d = json.loads(r.text)
    #get all items in the response which are average percipitation readings
    avg_prcp = [item for item in d['results'] if item['datatype']=='PRCP']
    #get the date field from all average temperature readings
    dates_prcp += [item['date'] for item in avg_prcp]
    #get the actual average temperature from all average temperature readings
    prcp += [item['value'] for item in avg_prcp]

#initialize dataframe
df_prcp = pd.DataFrame()

#populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
df_prcp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_prcp]
df_prcp['avgprcp'] = prcp
