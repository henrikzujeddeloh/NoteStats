import os
import sys
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Function to return creation time of file
def get_creation_time(path):
    return os.stat(path).st_birthtime

# Function to return modification time of file
def get_modification_time(path):
    return os.path.getmtime(path)

# Function to return size of file
def get_size(path):
    return os.stat(path).st_size



# Scans direcory given in excecution arguments 
folder_path = sys.argv[1]

# Creates pandas DataFrame with relevant colomns
df = pd.DataFrame(columns=('note', 'creation_time', 'modification_time', 'size'))

# Loops through all files in selected directory
i = 0
for filename in os.listdir(folder_path):
    # f is path to current file
    f = os.path.join(folder_path, filename)
    # checks if path is a file
    if os.path.isfile(f):
        creation = pd.to_datetime(int(get_creation_time(f)), utc='True', unit='s')
        modification = pd.to_datetime(int(get_modification_time(f)), utc='True', unit='s')
        size = get_size(f)
        # adds i-th row to df with note info
        df.loc[i] = [filename, creation, modification, size]
        i += 1

# defines some date functions
convert_tz = lambda x: x.to_pydatetime()
get_date = lambda x: '{}-{:02}-{:02}'.format(convert_tz(x).year, convert_tz(x).month, convert_tz(x).day)
get_month = lambda x: convert_tz(x).month

# adds column to dataframe with creation and modificatoin date
df['creation_date'] = df['creation_time'].map(get_date)
df['modification_date'] = df['modification_time'].map(get_date)

# adds column to dataframe with creation month
df['creation_month'] = df['creation_time'].map(get_month)

# adds days since last edit column
today = pd.to_datetime("now")
df['last_edit'] = -(pd.to_datetime(df['modification_date']) - today).dt.days

#print(df)


# Sets dimensions of graph
DPI = 100
WIDTH = 10
HEIGHT = 5

# creates new dataframe with number of notes created per day
creation_date = df.groupby(['creation_date']).size()
min_date = creation_date.index.min()
max_date = creation_date.index.max()
date_range = pd.date_range(min_date, max_date)
creation_date.index = pd.DatetimeIndex(creation_date.index)
creation_date = creation_date.reindex(date_range, fill_value=0)
print(creation_date)

# creates new dataframe with number of notes created per month
creation_month = df.groupby(['creation_month']).size()
print(creation_month)


# create histogram of days since last edit
plt.figure("Days since last edit histogram", figsize=[WIDTH,HEIGHT], dpi=DPI)
plt.hist(df["last_edit"], bins = 30, color='#63abdb')
plt.title("Days since last edit")
plt.xlabel("Days")


# creates plot of note creation by date
plt.figure("Note creation by date", figsize=[WIDTH,HEIGHT], dpi=DPI)
creation_date.plot(kind='line', linewidth=3, color='#63abdb')
plt.title("Note creation")
plt.xlabel("Date")
plt.ylabel("Count")

plt.show()
