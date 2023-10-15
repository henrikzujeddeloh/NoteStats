import os
import pandas as pd
import modules.utils as utils
import modules.constants as const

def create_df(folder):
    
    # Creates pandas DataFrame with relevant colomns
    data_frame = pd.DataFrame(columns=('note', 'creation_time', 'modification_time', 'size'))

    # Loops through all files in selected directory
    i = 0
    numfiles = len(os.listdir(folder))
    for filename in os.listdir(folder):
        if not filename.startswith('.'):
            # f is path to current file
            f = os.path.join(folder, filename)
            # checks if path is a file and not a hidden file (like .DS_Store)
            if os.path.isfile(f):
                creation = pd.to_datetime(int(utils.get_creation_time(f)), utc=True, unit='s').tz_convert(const.TIMEZONE)
                modification = pd.to_datetime(int(utils.get_modification_time(f)), utc=True, unit='s').tz_convert(const.TIMEZONE)
                size = utils.get_size(f)
                # adds i-th row to df with note info
                data_frame.loc[i] = [filename, creation, modification, size]
                i += 1
                #print("FILE: " + str(i) + " of " + str(numfiles), end='\r')
    return data_frame
