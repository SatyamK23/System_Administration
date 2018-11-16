import tkinter as tk
import os

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,askdirectory
from pathlib import Path
from os import listdir
from os.path import isfile, join

root=tk.Tk()
root.title('Log Files')

my_label = tk.Label(root, text="Facility:")
my_label.grid(row=1, column=0,padx=10,pady=10)

facility = StringVar(root)
facility.set("kern")
fcy = tk.OptionMenu(root, facility, "*", "kern", "user", "mail", "daemon","auth", "syslog","lpr", "news", "cron", "authprev",
"ftp", "mark", "local<0-7>")
fcy.grid(row=1,column=3,padx=10,pady=10)

my_label = tk.Label(root, text="Level:")
my_label.grid(row=2,column=0,padx=10,pady=10)
Level = StringVar(root)
Level.set("emerg") #default value
lvl = tk.OptionMenu(root, Level,"*", "none", "emerg", "alert", "crit", "err"," warning", "notice", "info", "debug")
lvl.grid(row=2,column=3,padx=10,pady=10)    

Lvlsym = StringVar(root)
Lvlsym.set("=")
lvlsyl = tk.OptionMenu(root, Level,"=","!")
lvlsyl.grid(row=2,column=2,padx=10,pady=10)

my_button = tk.Button(root, text="Ok")
my_button.grid(row=3,column=2,padx=10,pady=10)

my_button = tk.Button(root, text="Cancel",command=root.quit)
my_button.grid(row=3,column=3,padx=10,pady=10)
root.mainloop()

