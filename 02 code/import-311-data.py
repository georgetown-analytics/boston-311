# this file imports 311 data from the Analyze Boston website
# and creates a dataframe called df_311

# import libraries
import pandas as pd

# create a vector of URLs

urls = ["https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/94b499d9-712a-4d2a-b790-7ceec5c9c4b1/download/311_service_requests_2011.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/382e10d9-1864-40ba-bef6-4eea3c75463c/download/311_service_requests_2012.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/407c5cd0-f764-4a41-adf8-054ff535049e/download/311_service_requests_2013.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/bdae89c8-d4ce-40e9-a6e1-a5203953a2e0/download/311_service_requests_2014.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/c9509ab4-6f6d-4b97-979a-0cf2a10c922b/download/311_service_requests_2015.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/b7ea6b1b-3ca4-4c5b-9713-6dc1db52379a/download/311_service_requests_2016.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/30022137-709d-465e-baae-ca155b51927d/download/311_service_requests_2017.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/2be28d90-3a90-4af1-a3f6-f28c1e25880a/download/311_service_requests_2018.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/ea2e4696-4a2d-429c-9807-d02eb92e0222/download/311_service_requests_2019.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/6ff6a6fd-3141-4440-a880-6f60a37fe789/download/script_105774672_20210108153400_combine.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/f53ebccd-bc61-49f9-83db-625f209c95f5/download/tmppgq9965_.csv"
        , "https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/81a7b022-f8fc-4da5-80e4-b160058ca207/download/tmp53_2kemh.csv"
       ]

# import each csv
dfs = [pd.read_csv(url) for url in urls]

# combine into a single data frame
df_311 = pd.concat(dfs, ignore_index=True)

# fix a few of the columns
# convert the closed date to a date time format
df_311['closed_dt'] = pd.to_datetime(df_311['closed_dt'])

df_311['open_dt'] = pd.to_datetime(df_311['open_dt'])

# collapse dates down to month-year
df_311['close_date'] = df_311['closed_dt'].dt.to_period('M')

df_311['open_date'] = df_311['open_dt'].dt.to_period('M')

# create year columns
df_311['close_year'] = df_311['closed_dt'].dt.year

df_311['open_year'] = df_311['open_dt'].dt.year

# convert our closed variable to binary, 1/0
df_311['closed'] = df_311['case_status'].apply(lambda x: 1 if x=='Closed' else 0)

df_311['opened'] = df_311['case_status'].apply(lambda x: 1 if x=='Open' else 0)

# not recommended, but you can write this to a csv file
# df_311.to_csv("boston_311.csv", index = False)
