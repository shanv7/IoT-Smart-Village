"""
User Interface to Mangage the Warehouse

"""

# TODO: Open Files Automatically.

import tkinter as Tkinter
from admin_functions import add_farmer, add_crop, visualise, stock_left
from Company import company_buys
from Farmer_Produce import farmers_entry
from Price_Mining import update_price
import GUI_AddFarmers

top = Tkinter.Tk()

top.title("Warehouse Management System - Raspberry Pi")

w = 600  # width for the Tk root
h = 600  # height for the Tk root
ws = top.winfo_screenwidth()  # width of the screen
hs = top.winfo_screenheight()  # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
top.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Creating Buttons

A = Tkinter.Button(top, text="Visualise Database", command=visualise())
B = Tkinter.Button(top, text="Remaining Stock", command=stock_left())
C = Tkinter.Button(top, text="Update Price", command=update_price())
# D = Tkinter.Button(top, text="Add New Farmer", command=GUI_AddFarmers)
# E = Tkinter.Button(top, text="Farmer Adds New Produce", command=opentxtfile)
# F = Tkinter.Button(top, text="Companies Buy Produce", command=cobdd)
# G = Tkinter.Button(top, text="Add New Crop", command=ite_master)


A.pack()
B.pack()
C.pack()
# D.pack()
# E.pack()
# F.pack()
# G.pack()

top.mainloop()
