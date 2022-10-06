# this file imports Fire Incident Reporting data from the Analyze Boston website
# and creates a dataframe called df_311

# import libraries
import pandas as pd

# create a vector of URLs

urls = ["https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/4326ca95-09ec-42e0-8cee-f048e00e6728/download/property-assessment-fy12.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/425fd527-e26b-49c9-853c-1c4d3d2bdd97/download/property-assessment-fy13.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/7190b0a4-30c4-44c5-911d-c34f60b22181/download/property-assessment-fy2014.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/bdb17c2b-e9ab-44e4-a070-bf804a0e1a7f/download/property-assessment-fy2015.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/cecdf003-9348-4ddb-94e1-673b63940bb8/download/property-assessment-fy2016.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/062fc6fa-b5ff-4270-86cf-202225e40858/download/property-assessment-fy2017.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/fd351943-c2c6-4630-992d-3f895360febd/download/ast2018full.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/695a8596-5458-442b-a017-7cd72471aade/download/fy19fullpropassess.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/8de4e3a0-c1d2-47cb-8202-98b9cbe3bd04/download/data2020-full.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/c4b7331e-e213-45a5-adda-052e4dd31d41/download/data2021-full.csv"
        , "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/4b99718b-d064-471b-9b24-517ae5effecc/download/fy2022pa-4.csv"
       ]

# import each csv
dfs = [pd.read_csv(url) for url in urls]

# combine into a single data frame
df_propasess = pd.concat(dfs, ignore_index=True)

# not recommended, but you can write this to a csv file
# df_propasess.to_csv("property_asessment.csv", index = False)