import numpy as np
import pandas as pd
import seaborn as sns
from tabulate import tabulate
import matplotlib.pyplot as plt

import modules.constants as const


# defines some date functions
convert_tz = lambda x: x.to_pydatetime()
get_month = lambda x: convert_tz(x).month


def show_date(data_frame):

    # adds column to dataframe with creation and modificatoin date
    data_frame['creation_date'] = data_frame['creation_time'].dt.date

    # creates new dataframe with number of notes created per day
    creation_date = data_frame.groupby(['creation_date']).size()
    min_date = creation_date.index.min()
    max_date = creation_date.index.max()
    date_range = pd.date_range(min_date, max_date)
    creation_date.index = pd.DatetimeIndex(creation_date.index)
    creation_date = creation_date.reindex(date_range, fill_value=0)

    # creates plot of note creation by date
    fig_date, axs_date = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    creation_date.plot(ax=axs_date, kind='line', linewidth=3, color='#63abdb', title="Note creation", xlabel="Date", ylabel="Count")



def show_month(data_frame):

    # adds column to dataframe with creation month
    data_frame['creation_month'] = data_frame['creation_time'].map(get_month)

    # creates new dataframe with number of notes created per month
    creation_month = data_frame.groupby(['creation_month']).size()

    # creates plot of note creation by month
    fig_month, axs_month = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    creation_month.plot(kind='bar', ax=axs_month, title="Note Creation", xlabel="Month", ylabel="Count")
    axs_month.set_xticks(np.arange(0,12,1))
    axs_month.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])



def show_hist(data_frame):

    # adds days since last edit column
    data_frame['modification_date'] = data_frame['modification_time'].dt.date
    today = pd.to_datetime("now")
    data_frame['last_edit'] = -(pd.to_datetime(data_frame['modification_date']) - today).dt.days

    # create histogram of days since last edit
    BIN_WIDTH = 5
    bins = np.arange(0, data_frame['last_edit'].max()+BIN_WIDTH, BIN_WIDTH)
    fig_hist, axs_hist = plt.subplots(figsize=[const.WIDTH, const.HEIGHT])
    data_frame["last_edit"].plot(ax=axs_hist, kind='hist', bins = bins, color='#63abdb', edgecolor='black',  linewidth=1, title="Days since last edit", xlabel="Days")
    top_5 = data_frame.sort_values(by='last_edit', ascending=False).head(5)
    print("5 Oldest Notes: \n" + tabulate(top_5[['note','last_edit']], headers=['Note', 'Last Edit (days)'], tablefmt='psql', showindex=False))



def show_size(data_frame):

    # sorts notes by size
    data_frame = data_frame.sort_values(by='size', ascending=False)
    
    # converts bytes to kilobytes
    data_frame['size'] = data_frame['size']/1000
    
    # creates histogram
    BIN_WIDTH = 0.5
    bins = np.arange(0, data_frame['size'].max()+BIN_WIDTH, BIN_WIDTH)
    fig_size, axs_size = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    data_frame["size"].plot(ax=axs_size, kind='hist', bins=bins, color='#63abdb', edgecolor='black',  linewidth=1, title="Note Size", xlabel="Size (KiB)")
    top_5 = data_frame.head(5)
    print("5 Largest Notes: \n" + tabulate(top_5[['note', 'size']], headers=['Note', 'Size (KiB)'], tablefmt='psql', showindex=False))
    print("Total note library size: " +  str(round(data_frame['size'].sum(), 1)) + " KiB")    


def show_heatmap(data_frame):
    
    # add weekday coloumn
    data_frame["weekday"] = data_frame["modification_time"].dt.day_name()
    
    # put weekdays in correct order (starting with monday
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    data_frame['weekday'] = pd.Categorical(data_frame['weekday'], categories=week_days, ordered=True)
    data_frame = data_frame.sort_values('weekday')
    
    # add hour of day column
    data_frame["hour"] = data_frame["modification_time"].dt.hour
    print(data_frame) 
    # creates new pivot table with hour of day and day of week
    hour_weekday = data_frame.groupby(["weekday", "hour"]).size().unstack()
    
    # create heatmap
    fig_heatmap, axs_heatmap = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    sns.heatmap(hour_weekday, cmap="Blues", ax=axs_heatmap)
    axs_heatmap.set_title("Modification Time")
