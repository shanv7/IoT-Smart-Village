"""
Mining Price of Commodities from Agmarknet

To get a list of Commodities Produced in your area:
http://www.agmarknet.nic.in/agnew/NationalBEnglish/rpt5CommodityDailyReport.aspx

"""

import os
import pandas as pd
import numpy as np
import time
import datetime
import requests


def update_price():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    date = str(int(st[8:10])-1)+"/"+st[5:7]+"/"+st[0:4]
    # print(date)

    price_dict = dict()

    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df1 = pd.read_csv(path)
    commodity_list = list(df1)[4:]
    # print(commodity_list)

    for commodity in commodity_list:

        # commodity = "Banana"
        website = "http://agmarknet.nic.in/cmm2_home.asp?comm="+commodity+"&dt="+date

        html = requests.get(website).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        # print(df)

        # Removing Everything but Mangalore

        markets = np.array(df[0].tolist())

        index_mangalore = np.argwhere(markets == "Mangalore")[0][0]
        modal_price = int(df.loc[index_mangalore, len(list(df))-1])

        price_dict[commodity] = modal_price
        # print(commodity, modal_price)

    print(price_dict)
    prices = pd.DataFrame(list(price_dict.items()), columns=["Commodity", "Price"])
    writer = pd.ExcelWriter('Prices.xlsx', engine='xlsxwriter')
    prices.to_csv("Prices.csv", index=False)
    prices.to_excel(writer, sheet_name='Prices', index=False)

update_price()
