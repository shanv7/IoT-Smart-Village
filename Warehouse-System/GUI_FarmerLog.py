from tkinter import *
from Farmer_Produce import farmers_entry

fields = 'Aadhar Number', 'Crop', 'Quantity'


def fetch(entries):
    # field = entry[0]
    aadhar = int(entries[0][1].get())
    crop = entries[1][1].get()
    qty = int(entries[2][1].get())
    farmers_entry(aadhar, crop, qty)


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


def Farmer_Log():
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Add',
                command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()

# Farmer_Log()
