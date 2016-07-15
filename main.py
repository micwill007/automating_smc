from modules import *
import time, sys, json
from tkinter import *


###############################################
#
#   WARNING: Don't run scraping scripts unless
#   the two accounts are THE SAME
#
###############################################

with open('./config.json') as data_file:
  data = json.load(data_file)

user = data['username']
passw = data['password']
path = data['driverlocation']

def callback():
  a = e.get()
  b = f.get()
  if (var.get()):
    synonym.runSynonym(a, b, path, user, passw) 

  if (var2.get()):
    fieldSettingText.runFieldSettingText(b, path, user, passw)

  if (var3.get()):
    fieldSettings.runFieldSettings(a, b, path, user, passw)

  if (var4.get()):
    fieldFaceting.runFieldFaceting(a, b, path, user, passw)

master = Tk()
e = Entry(master)
e.insert(0, "scrape")
e.pack()

f = Entry(master)
f.insert(0, "site")
f.pack()

var = IntVar()
c = Checkbutton(master, text="synonym", variable=var)
c.pack(side=LEFT)

var2 = IntVar()
c2 = Checkbutton(master, text="fieldtext", variable=var2)
c2.pack(side=LEFT)

var3 = IntVar()
c3 = Checkbutton(master, text="fieldsettings", variable=var3)
c3.pack(side=LEFT)

var4 = IntVar()
c4 = Checkbutton(master, text="fieldfaceting", variable=var4)
c4.pack(side=LEFT)


e.focus_set()

b = Button(master, text="Run", width=10, command=callback)
b.pack()

mainloop()
#comment this out if u wanna stay on the page
#browser.quit()