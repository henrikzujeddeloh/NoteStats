import os
import datetime
import argparse
import tracemalloc
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

# Sets dimensions of graph
DPI = 100
WIDTH = 10
HEIGHT = 5


# Function to return creation time of file
def get_creation_time(path):
    return os.stat(path).st_birthtime

# Function to return modification time of file
def get_modification_time(path):
    return os.path.getmtime(path)

# Function to return size of file
def get_size(path):
    return os.stat(path).st_size

def create_df(folder):
    
    # Creates pandas DataFrame with relevant colomns
    data_frame = pd.DataFrame(columns=('note', 'creation_time', 'modification_time', 'size'))

    # Loops through all files in selected directory
    i = 0
    for filename in os.listdir(folder):
        if not filename.startswith('.'):
            # f is path to current file
            f = os.path.join(folder, filename)
            # checks if path is a file and not a hidden file (like .DS_Store)
            if os.path.isfile(f):
                creation = pd.to_datetime(int(get_creation_time(f)), utc='True', unit='s')
                modification = pd.to_datetime(int(get_modification_time(f)), utc='True', unit='s')
                size = get_size(f)
                # adds i-th row to df with note info
                data_frame.loc[i] = [filename, creation, modification, size]
                i += 1
    return data_frame

def show_date(data_frame):

    # adds column to dataframe with creation and modificatoin date
    data_frame['creation_date'] = data_frame['creation_time'].map(get_date)

    # creates new dataframe with number of notes created per day
    creation_date = data_frame.groupby(['creation_date']).size()
    min_date = creation_date.index.min()
    max_date = creation_date.index.max()
    date_range = pd.date_range(min_date, max_date)
    creation_date.index = pd.DatetimeIndex(creation_date.index)
    creation_date = creation_date.reindex(date_range, fill_value=0)

    # creates plot of note creation by date
    plt.figure("Note creation by date", figsize=[WIDTH,HEIGHT], dpi=DPI)
    creation_date.plot(kind='line', linewidth=3, color='#63abdb')
    plt.title("Note creation")
    plt.xlabel("Date")
    plt.ylabel("Count")


def show_month(data_frame):

    # adds column to dataframe with creation month
    data_frame['creation_month'] = data_frame['creation_time'].map(get_month)

    # creates new dataframe with number of notes created per month
    creation_month = data_frame.groupby(['creation_month']).size()

    # creates plot of note creation by month
    plt.figure("Note creation by month", figsize=[WIDTH,HEIGHT], dpi=DPI)
    creation_month.plot(kind='bar')
    plt.title("Note creation")
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


def show_hist(data_frame):

    # adds days since last edit column
    data_frame['modification_date'] = data_frame['modification_time'].map(get_date)
    today = pd.to_datetime("now")
    data_frame['last_edit'] = -(pd.to_datetime(df['modification_date']) - today).dt.days

    # create histogram of days since last edit
    BIN_WIDTH = 5
    plt.figure("Days since last edit histogram", figsize=[WIDTH,HEIGHT], dpi=DPI)
    bins = np.arange(0, data_frame['last_edit'].max(), BIN_WIDTH)
    plt.hist(data_frame["last_edit"], bins = bins, color='#63abdb', edgecolor='black',  linewidth=1)
    plt.title("Days since last edit")
    plt.xlabel("Days")
    top_5 = data_frame.sort_values(by='last_edit', ascending=False).head(5)
    print("5 Oldest Notes: \n" + tabulate(top_5[['note','last_edit']], headers=['Note', 'Last Edit (days)'], tablefmt='psql', showindex=False))

def show_size(data_frame):

    # sorts notes by size
    data_frame = data_frame.sort_values(by='size', ascending=False)
    
    # converts bytes to kilobytes
    data_frame['size'] = data_frame['size']/1000
    
    # creates histogram
    BIN_WIDTH = 0.2
    plt.figure("File size histogram", figsize=[WIDTH,HEIGHT], dpi=DPI)
    bins = np.arange(0, data_frame['size'].max(), BIN_WIDTH)
    plt.hist(data_frame["size"], bins=bins, color='#63abdb', edgecolor='black',  linewidth=1)
    plt.title("Note size")
    plt.xlabel("Size (KiB)")
    top_5 = data_frame.head(5)
    print("5 Largest Notes: \n" + tabulate(top_5[['note', 'size']], headers=['Note', 'Size (KiB)'], tablefmt='psql', showindex=False))
    

# defines some date functions
convert_tz = lambda x: x.to_pydatetime()
get_date = lambda x: '{}-{:02}-{:02}'.format(convert_tz(x).year, convert_tz(x).month, convert_tz(x).day)
get_month = lambda x: convert_tz(x).month



# parses passed arguments
parser = argparse.ArgumentParser()
parser.add_argument("folder_path", help="path to notes direcotry which should be scanned")
parser.add_argument("--hist", help="output days since last edit histogram", action="store_true")
parser.add_argument("--date", help="output creation by date plot", action="store_true")
parser.add_argument("--month", help="output creation by month plot", action="store_true")
parser.add_argument("--size", help="output note by size bar graph", action="store_true")
args = parser.parse_args()



df = create_df(args.folder_path)



if args.date:
    show_date(df)

if args.month:
    show_month(df)

if args.hist:
    show_hist(df)

if args.size:
    show_size(df)

# prints memory usage of dataframe
print(df.info(memory_usage="deep"))
plt.show()
