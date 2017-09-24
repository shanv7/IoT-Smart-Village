"""
User Interface to Mangage the Warehouse

"""

import tkinter as Tkinter
from admin_functions import *
from Company import company_buys
from Farmer_Produce import farmers_entry

top = Tkinter.Tk()

top.title("Warehouse Management System - Raspberry Pi")

w = 200  # width for the Tk root
h = 800  # height for the Tk root
ws = top.winfo_screenwidth()  # width of the screen
hs = top.winfo_screenheight()  # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
top.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Creating Buttons
A = Tkinter.Button(top, text="Farmer Adds New Produce", command=opentxtfile)
B = Tkinter.Button(top, text="Companies Buy Produce", command=cobdd)
C = Tkinter.Button(top, text="Add New Farmer", command=robdd)
D = Tkinter.Button(top, text="Add New Crop", command=ite_master)
E = Tkinter.Button(top, text="Database", command=visualise())
F = Tkinter.Button(top, text="Remaining Stock", command=stock_left())
G = Tkinter.Button(top, text="Update Price", command=())

A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
G.pack()

top.mainloop()