# import dependencies
import numpy as np
import pandas as pd
import lasio
import os
import shutil

def get_file_names(data_dir):
    '''
    Input : directory of data, string
    Output : Return List, names of all files present in directory

    '''
    f_names = os.listdir(data_dir)
    print(f"Files in the directory : {f_names[0:100]} ....")
    return f_names

def read_files_in(data_dir):
    '''
    Input : String, directory name where data is present
    Output : Dataframe, concatenated logs of all logs

    This function will return the concatenated data of all the logs present in the 
    directory. The missing values are replaced with NaN.
    '''
    f_names = get_file_names(data_dir)
    df_list = []
    for fname in f_names:
        f_path = os.path.join(data_dir, fname)
        f = lasio.read(f_path,ignore_header_errors=True)
        print(f"Scanning file {f_path}")
        df = f.df()
        df_list.append(df)
    print(f"Number of files scanned = {len(df_list)}")
    dataframe = pd.concat(df_list,axis=0)
    return dataframe
