from tkinter import *
from admin_functions import add_farmer

fields = 'Name', 'Aadhar Number', 'eMail', 'Phone'


def fetch(entries):
    # field = entry[0]
    name = entries[0][1].get()
    aadhar = int(entries[1][1].get())
    email = entries[2][1].get()
    phone = int(entries[3][1].get())
    add_farmer(name, aadhar, email, phone)


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


def Add_Farmers():
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Add',
                command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()

# Add_Farmers()
