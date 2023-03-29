import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_creation_time(path):
    return os.stat(path).st_birthtime

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()

df = pd.DataFrame(columns=('note', 'creation_time'))

i = 0
for filename in os.listdir(folder_path):
    f = os.path.join(folder_path, filename)
    if os.path.isfile(f):
        creation = pd.to_datetime(int(get_creation_time(f)), utc='True', unit='s')
        df.loc[i] = [filename, creation]
        i += 1

convert_tz = lambda x: x.to_pydatetime()
get_date = lambda x: '{}-{:02}-{:02}'.format(convert_tz(x).year, convert_tz(x).month, convert_tz(x).day)
get_month = lambda x: convert_tz(x).month

df['creation_date'] = df['creation_time'].map(get_date)
df['creation_month'] = df['creation_time'].map(get_month)
print(df)

DPI = 100
WIDTH = 10
HEIGHT = 5


creation_date = df.groupby(['creation_date']).size().rename('count')
print(creation_date)
creation_month = df.groupby(['creation_month']).size().rename('count')
print(creation_month)

plt1 = plt.subplots(figsize=(WIDTH, HEIGHT), dpi=DPI)


plt1 = creation_date.plot(kind='line', figsize=[WIDTH,HEIGHT], linewidth=4, alpha=1, marker='o', color='b',markeredgecolor='r', markerfacecolor='w', markersize=8, markeredgewidth=2)

plt1.set_title("Note creation")
plt1.set_xlabel("Date")
plt1.set_ylabel("Count")
plt.show()
