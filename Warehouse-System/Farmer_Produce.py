"""
To create a SQLite Database that can be queried.

"""

import pandas as pd
import os
import numpy as np
import time
import datetime
import csv

# TODO: Change Crop Names, Farmer Names.


def farmers_entry(aadhar_number, crop, qty):

    with open('Prices.csv', mode='r') as infile:
        reader = csv.reader(infile)
        with open('Temporary_Data.csv', mode='w') as outfile:
            price_dict = {rows[0]: rows[1] for rows in reader}

    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df = pd.read_csv(path)
    # print(df)

    # Add to Existing Crops

    aadhar_list = np.array(df["Aadhar Number"].tolist()).astype(int)

    rowpos = np.argwhere(aadhar_list == aadhar_number)
    print(rowpos[0][0])

    df.loc[rowpos[0][0], crop] += qty

    df.to_csv(path, index=False)
    print(df)

    # Logging

    name = df.loc[rowpos[0][0], "Name"]

    log_path = os.path.abspath("Farmers_Events_Log.csv")
    logf = pd.read_csv(log_path)
    # print(logf)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # print(st)

    append_list = [[st, name, aadhar_number, crop, qty]]
    logf = logf.append(pd.DataFrame(append_list, columns=["Timestamp", "Name", "Aadhar Number", "Crop", "Quantity"]),
                       ignore_index="True")

    logf.to_csv(log_path, index=False)
    # print(logf)

    return price_dict[crop]

r = farmers_entry(12345, "Banana", 100)
print(r)
