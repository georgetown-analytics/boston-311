# Intro
# This file scrapes contribution data from https://www.ocpf.us/Home/Index
# for the city of Boston from 2011 to Present and stores them in a data frame called
# df_contrib


# Set up---------
# load libraries
import os
import json
import requests
import pandas as pd
from pprintpp import pprint as pp
from pandas import json_normalize

# Data ingestion prep----------------
# there are just under 3.9 million observations in the data according to the OCPF website
# create a counter of numbers to generate urls
a = list(range(100, 391900, 100))

# convert the list from numeric to string values for ease of concatenation
a = [str(x) for x in a]

# Pull data------------

# create an empty object
url = []

# for each item in our list of numbers create a url
for number in a:
   url.append('https://www.ocpf.us/ReportData/GetItemsAndSummary?pageSize=100&currentIndex=' + number + '&sortField=date&sortDirection=DESC&searchTypeCategory=A&recordTypeId=201&cityCode=35&startDate=01/01/2011&filerCpfId=0')

# call the urls
results = [requests.get(u) for u in url]

# write to structured json files
results_decode = map(lambda x: x.json(),results)

# output to a dataframe
df_contrib = json_normalize(results_decode,'items')
