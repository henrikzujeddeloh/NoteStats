import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def get_creation_time(path):
    return os.stat(path).st_birthtime

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()

df = pd.DataFrame(columns=('note', 'creation'))

i = 0
for filename in os.listdir(folder_path):
    f = os.path.join(folder_path, filename)
    if os.path.isfile(f):
        creation = pd.to_datetime(int(get_creation_time(f)), utc='True', unit='s')
        df.loc[i] = [filename, creation]
        i += 1
print(df)


