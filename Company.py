"""
Function to enable companies to buy stocks from the Warehouse

"""

import pandas as pd
import os
import numpy as np
import time
import datetime
import smtplib

name_of_crops = ["Crop 1", "Crop 2", "Crop 3", "Crop 4", "Crop 5", "Crop 6"]
price_of_crops = [1000, 2000, 1500, 3000, 5000, 2500]
price_dict = dict(zip(name_of_crops, price_of_crops))


def company_buys(name, crop, qty):

    path = os.path.abspath("Farmers_Data_Is_In_This_File.csv")
    df = pd.read_csv(path)

    price = price_dict[crop]  # Stock of Required Crop
    croplist = np.array(df[crop].tolist())
    sum1 = np.sum(croplist)
    # print(sum1)

    if qty <= sum1:

        contribution = croplist/sum1
        # print(contribution)

        new_croplist = croplist - contribution*qty
        df_append = pd.DataFrame(new_croplist)
        money_earned = contribution*qty*price
        df[crop] = df_append[0]  # TODO
        # print(df)

        df.to_csv(path, index=False)

        # LOGGING

        price_company = qty * price

        log_path = os.path.abspath("Company_Events_Log.csv")
        logf = pd.read_csv(log_path)

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        append_list = [[st, name, crop, qty, price_company]]
        logf = logf.append(pd.DataFrame(append_list, columns=["Timestamp", "Name", "Crop", "Quantity", "Price"]),
                           ignore_index="True")
        logf.to_csv(log_path, index=False)

        # MAILING

        # all_email_list = df["eMail ID"].tolist()
        # print(all_email_list)
        # email_list = list()
        # money_earned_list = list()
        # for ijk in range(len(contribution)):
        #     if contribution[ijk] > 0:
        #         email_list.append(all_email_list[ijk])
        #         money_earned_list.append(money_earned[ijk])
        # # print(email_list)
        # # print(money_earned_list)
        #
        # smtp_user = "warehousempproject@gmail.com"
        # smtp_pass = "Thisisawarehouse"
        # subject = "Your Crops have been bought"
        #
        # s = smtplib.SMTP("smtp.gmail.com", 587)
        # s.ehlo()
        # s.starttls()
        # s.ehlo()
        # s.login(smtp_user, smtp_pass)
        #
        # for i in range(len(email_list)):
        #     header = "To: " + email_list[i] + "\nFrom: " + smtp_user + "\nSubject: " + subject
        #     body = "Rupees " + str(money_earned_list[i]) + " has been added to your account"
        #     s.sendmail(smtp_user, email_list[i], header + "\n\n" + body)
        #
        # s.quit()

    else:
        print("Sorry! Stock of "+crop+" Left: "+str(sum1))

company_buys("Nestle", "Crop 5", 10)
