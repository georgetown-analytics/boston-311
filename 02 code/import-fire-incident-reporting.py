# this file imports Fire Incident Reporting data from the Analyze Boston website
# and creates a dataframe called df_311

# import libraries
import pandas as pd

# create a vector of URLs

urls = ["https://data.boston.gov/dataset/ac9e373a-1303-4563-b28e-29070229fdfe/resource/64d6aa98-a3aa-4080-a316-b6d493082091/download/2012-bostonfireincidentopendata.csv"
        , "https://data.boston.gov/dataset/ac9e373a-1303-4563-b28e-29070229fdfe/resource/76771c63-2d95-4095-bf3d-5f22844350d8/download/2013-bostonfireincidentopendata.csv"
        , "https://data.boston.gov/dataset/ac9e373a-1303-4563-b28e-29070229fdfe/resource/91a38b1f-8439-46df-ba47-a30c48845e06/download/tmpkf9eytdj.csv"
       ]

# import each csv
dfs = [pd.read_csv(url) for url in urls]

# combine into a single data frame
df_fireinci = pd.concat(dfs, ignore_index=True)

# not recommended, but you can write this to a csv file
# df_fireinci.to_csv("fire_incident_reporting.csv", index = False)