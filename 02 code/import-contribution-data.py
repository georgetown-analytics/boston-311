# Intro
# This file scrapes contribution data from https://www.ocpf.us/Home/Index
# for the city of Boston from 2011 to Present and stores them in a data frame called
# df_contrib


# Set up---------
# load libraries
import requests
import pandas as pd
from tqdm.notebook import tqdm

# create a header object for the scraping
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

# define a session object to keep our scraping going
s = requests.Session()
# update headers
s.headers.update(headers)

# create dataframe object
df_contrib = pd.DataFrame()


for x in tqdm(range(1, 391900, 100)):
    url = f'https://www.ocpf.us/ReportData/GetItemsAndSummary?pageSize=100&currentIndex={x}&sortField=date&sortDirection=DESC&searchTypeCategory=A&recordTypeId=201&cityCode=35&startDate=01/01/2011&filerCpfId=0'
    r = s.get(url)
    df = pd.json_normalize(r.json()['items'])
    df_contrib = pd.concat([df_contrib, df], axis=0, ignore_index=True)
