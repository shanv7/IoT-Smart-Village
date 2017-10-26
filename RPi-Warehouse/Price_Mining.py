import urllib
from bs4 import BeautifulSoup

import os
import pandas as pd
import time
import datetime


"""
Mining Price of Commodities from Agmarknet

Finds Latest Price of a commodity from real time Indian Government Website agmarknet

Important Note:
To get a list of Commodities Produced in your area:
http://www.agmarknet.nic.in/agnew/NationalBEnglish/CommodityDailyStateWise.aspx?ss=2

Outputs:
Updates Prices.xlsx, Prices.csv

"""


def update_price():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y')
    # print(st)

    price_dict = dict()

    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df1 = pd.read_csv(path)
    commodity_list = list(df1)[4:]
    print(commodity_list)

    comlist2 = commodity_list[:]
    for i in range(len(comlist2)):
        comlist2[i] = comlist2[i].replace(" ", "%20")

    print(comlist2)

    for commodity in comlist2:
        date = st
        for i in range(1, 100):
            website = "http://agmarknet.nic.in/cmm2_home.asp?comm="+commodity+"&dt="+date
            print(website)
            try:
                html = urllib.request.urlopen(website).read()
                # print("Line 1")
                soup = BeautifulSoup(html, 'lxml')
                # print("Line 2")
                f = open("Web.txt", "w")
                f.write(soup.get_text())
                # print("Line 3")
                f.close()

                f = open("Web.txt", "r")
                for num, line in enumerate(f):
                    if "Mangalore" in line:
                        # print(num)
                        index = num + 7
                        break
                f.close()
                f = open("Web.txt", "r")
                data = f.readlines()
                index7 = data[index].replace(" ", "")
                index8 = data[index + 1].replace(" ", "")
                if index7 == "\n":
                    index7 = "1000000"
                if index8 == "\n":
                    index8 = "1000000"
                # print(index7, index8)
                if int(index7) > int(index8):
                    index = index8
                else:
                    index = index7
                modal_price = int(index)
                print(index)
                price_dict[commodity.replace("%20", " ")] = modal_price
                break
            except:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d')
                theday = datetime.date(*map(int, date.split('/')))
                prevday = theday - datetime.timedelta(days=i)
                date = prevday.strftime('%d/%m/%Y')
                print(date)
                continue

        # print(commodity, modal_price)

    # print(price_dict)
    prices = pd.DataFrame(list(price_dict.items()), columns=["Commodity", "Price"])
    # writer = pd.ExcelWriter('Prices.xlsx', engine='xlsxwriter')
    prices.to_csv("Prices.csv", index=False)
    # prices.to_excel(writer, sheet_name='Prices', index=False)
    os.system("xdg-open Prices.csv")

# update_price()

