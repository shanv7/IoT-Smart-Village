"""
User Interface to Mangage the Warehouse

"""

# TODO: Open Files Automatically.

import tkinter as Tkinter
from tkinter import *
from admin_functions import visualise, stock_left
from Price_Mining import update_price
from GUI_AddFarmers import Add_Farmers
from GUI_AddCrop import Add_Crops
from GUI_FarmerLog import Farmer_Log
from GUI_Company import company_buy

top = Tkinter.Tk()

top.title("Warehouse Management System - Raspberry Pi")

# Creating Buttons

A = Tkinter.Button(top, text="Visualise Database", command=lambda: visualise())
B = Tkinter.Button(top, text="Remaining Stock", command=lambda: stock_left())
C = Tkinter.Button(top, text="Update Price", command=lambda: update_price())
D = Tkinter.Button(top, text="Add New Farmer", command=lambda: Add_Farmers())
E = Tkinter.Button(top, text="Add New Crop", command=lambda: Add_Crops())
F = Tkinter.Button(top, text="Farmer Log", command=lambda: Farmer_Log())
G = Tkinter.Button(top, text="Buy Crops", command=lambda: company_buy())

F.pack()
G.pack()
A.pack(side=LEFT, padx=5, pady=5)
B.pack(side=LEFT, padx=5, pady=5)
C.pack(side=LEFT, padx=5, pady=5)
D.pack(side=LEFT, padx=5, pady=5)
E.pack(side=LEFT, padx=5, pady=5)

top.mainloop()
