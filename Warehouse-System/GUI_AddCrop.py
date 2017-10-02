from tkinter import *
from admin_functions import add_crop
import webbrowser

fields = ['Crop Name']


def fetch(entries):
    name = entries[0][1].get()
    add_crop(name)


def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries


def Add_Crops():
    root = Tk()
    # webbrowser.open("http://www.agmarknet.nic.in/agnew/NationalBEnglish/CommodityDailyStateWise.aspx?ss=2")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Add',
                command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Crops in Mangalore',
                command=lambda:
                webbrowser.open("http://www.agmarknet.nic.in/agnew/NationalBEnglish/CommodityDailyStateWise.aspx?ss=2"))
    b3.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()

Add_Crops()
