import tkinter as tk
import os

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,askdirectory
from pathlib import Path
from os import listdir
from os.path import isfile, join
from tkinter import font

root=tk.Tk()
root.title('Log Files')

logfile = StringVar() 
def setlog():
    f = facility.get()
    l = Level.get()
    s = Lvlsym.get()
    fileName = logfile.get()
    cmd = "sudo -S touch "+fileName
    print(cmd)
    os.system(cmd)

    logline = f+"."+s+l+"    "+fileName
    cwd = os.getcwd()
    cmd2 = "chmod 777 manageLog.sh"
    print(cmd2)
    os.system(cmd2)
    cmd3 = "sudo -S ./manageLog.sh "+logline
    print(cmd3)
    os.system(cmd3)

my_label = tk.Label(root, text="Facility:")
my_label.grid(row=1, column=0,padx=10,pady=10)

facility = StringVar(root)
facility.set("kern")
fcy = tk.OptionMenu(root, facility, "*", "kern", "user", "mail", "daemon","auth", "syslog","lpr", "news", "cron", "authprev",
"ftp", "mark", "local0","local1","local2","local3","local4","local5","local6","local7")
#fcy.config(font=helv36)
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

my_label = tk.Label(root, text="Select a log file to store entries")
my_label.grid(row=3,column=0,padx=10,pady=10)
my_entry = tk.Entry(root, textvariable=logfile, bd=3, bg="white")
my_entry.grid(row=3,column=2)        
                                                                         
my_button = tk.Button(root, text="Ok")
my_button.grid(row=4,column=2,padx=10,pady=10)

my_button = tk.Button(root, text="Cancel",command=root.quit)
my_button.grid(row=4,column=3,padx=10,pady=10)

root.mainloop()


