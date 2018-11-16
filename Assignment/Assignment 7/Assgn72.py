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

my_label = tk.Label(root, text="Select a log file:")
my_label.grid(row=1, column=0,padx=10,pady=10)
my_entry = tk.Entry(root, text="")
my_entry.grid(row=1,column=1,padx=10,pady=10)


my_label = tk.Label(root, text="Log Rotation:")
my_label.grid(row=2, column=0,padx=10,pady=10)


v = tk.StringVar()
v.set("S") # initialize
size = tk.Radiobutton(root, text='Size', variable=v)
size.config(anchor=W, bd=4, value='Size')
size.grid(row=3, column=1,padx=10,pady=10)
size_entry = tk.Entry(root)
size_entry.grid(row=3,column=2,padx=10,pady=10)

time = tk.Radiobutton(root, text='Time', variable=v)
time.config(anchor=W, bd=4, value='Time')
time.grid(row=4, column=1,padx=10,pady=10)
time_set = StringVar(root)
time_set.set("daily")
settime = tk.OptionMenu(root,time_set,"daily","weekly","monthly")
settime.grid(row=4,column=2,padx=10,pady=10)
my_label = tk.Label(root, text="Maximum number of log files")
my_label.grid(row=5, column=0,padx=10,pady=10)
my_entry1 = tk.Entry(root)
my_entry1.grid(row=5,column=1,padx=10,pady=10)

#comp = tk.Radiobutton(root, text='Compression', variable=v)
#comp.config(anchor=W, bd=4, value='Compression')
comp_label = tk.Label(root, text="Compression")
comp_label.grid(row=6, column=0,padx=10,pady=10)
comp_set = StringVar(root)
comp_set.set("compress")
comps = tk.OptionMenu(root,time_set,"compress","delay compress")
comps.grid(row=6,column=1,padx=10,pady=10)
my_button = tk.Button(root, text="Ok")
my_button.grid(row=7,column=1,padx=10,pady=10)

my_button = tk.Button(root, text="Cancel",command=root.quit)
my_button.grid(row=7,column=2,padx=10,pady=10)
root.mainloop()
