"""
Mining Price of Commodities from Agmarknet

Finds Latest Price of a commodity from real time Indian Government Website agmarknet

Important Note:
To get a list of Commodities Produced in your area:
http://www.agmarknet.nic.in/agnew/NationalBEnglish/CommodityDailyStateWise.aspx?ss=2

Outputs:
Updates Prices.xlsx, Prices.csv

"""

import os
import pandas as pd
import numpy as np
import time
import datetime
import requests


def update_price():

    os.system("scp pi@technopi.local:Warehouse/Farmers_Data_Is_In_This_File.csv /Users/Shantanu/Documents/git/Warehouse-System")
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y')
    # print(st)

    price_dict = dict()

    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df1 = pd.read_csv(path)
    commodity_list = list(df1)[4:]
    # print(commodity_list)

    for commodity in commodity_list:

        markets = []
        date = st
        for i in range(1, 100):
            website = "http://agmarknet.nic.in/cmm2_home.asp?comm="+commodity+"&dt="+date
            print(website)

            html = requests.get(website).content
            try:
                df_list = pd.read_html(html)
                df = df_list[-1]
                # print(df)

                # Removing Everything but Mangalore

                markets = np.array(df[0].tolist())
                if "Mangalore" in markets:
                    break
                else:
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d')
                    theday = datetime.date(*map(int, date.split('/')))
                    prevday = theday - datetime.timedelta(days=i)
                    date = prevday.strftime('%d/%m/%Y')
                    print(date)
                    continue
            except:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d')
                theday = datetime.date(*map(int, date.split('/')))
                prevday = theday - datetime.timedelta(days=i)
                date = prevday.strftime('%d/%m/%Y')
                print(date)
                continue

        index_mangalore = np.argwhere(markets == "Mangalore")[0][0]
        modal_price = int(df.loc[index_mangalore, len(list(df))-1])

        price_dict[commodity] = modal_price
        # print(commodity, modal_price)

    # print(price_dict)
    prices = pd.DataFrame(list(price_dict.items()), columns=["Commodity", "Price"])
    # writer = pd.ExcelWriter('Prices.xlsx', engine='xlsxwriter')
    prices.to_csv("Prices.csv", index=False)
    # prices.to_excel(writer, sheet_name='Prices', index=False)
    os.system("open Prices.csv")

    os.system("scp /Users/Shantanu/Documents/git/Warehouse-System/Prices.csv pi@technopi.local:Warehouse/")
# update_price()
