"""
Admin Functions such as Stock left in every Crop,Visualising this data,
Viewing Current Prices, Adding New Crops & Farmers

"""

import pandas as pd
import os
import numpy as np


def stock_left():
    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df = pd.read_csv(path)

    crops = list(df)[4:]
    sum1 = list()

    for crop in crops:
        croplist = np.array(df[crop].tolist())
        sum1.append(np.sum(croplist))

    print_obj = "\n".join("{}    \t{}".format(k, v) for k, v in zip(crops, sum1))
    # print(print_obj)
    f = open("Remaining Stock.txt", "w")
    f.write(print_obj)

stock_left()


def add_farmer(name, aadhar, email, phone):
    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df = pd.read_csv(path)

    crop_init = list(np.zeros(len(list(df)[4:])))
    append_list = [name, aadhar, email, phone]
    for ijk in range(len(crop_init)):
        append_list.append(crop_init[ijk])
    # print(append_list)

    df = df.append(pd.DataFrame([append_list], columns=list(df)), ignore_index="True")
    # print(df)
    df.to_csv(path, index=False)

# add_farmer("F6", 12341, "arvind0422@gmail.com", 9781110001)


def add_crop(crop_name):
    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df = pd.read_csv(path)
    new_column = pd.DataFrame(np.zeros(len(df["Name"])))
    df[crop_name] = new_column[0]
    # print(df)
    df.to_csv(path, index=False)

# add_crop("Crop 6")


def visualise():
    path1 = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df1 = pd.read_csv(path1)
    path2 = os.path.abspath("Farmers_Events_Log.csv")
    df2 = pd.read_csv(path2)
    path3 = os.path.abspath("Company_Events_Log.csv")
    df3 = pd.read_csv(path3)
    writer = pd.ExcelWriter('Warehouse.xlsx', engine='xlsxwriter')
    df1.to_excel(writer, sheet_name='Farmers Database', index=False)
    df2.to_excel(writer, sheet_name='Farmers Log', index=False)
    df3.to_excel(writer, sheet_name='Companies Log', index=False)
    writer.save()

# visualise()
