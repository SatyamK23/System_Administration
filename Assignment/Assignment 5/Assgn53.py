import tkinter as tk
import os  
import subprocess as sub

from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

root = tk.Tk()
myFont = Font(family="Times New Roman", size=12)
def original_nice():
    p=sub.Popen('./nice_display.sh',stdout=sub.PIPE, stderr=sub.PIPE)
    output,errors = p.communicate()
    text = tk.Text(root)
    text.grid_forget()
    text.grid(row=1,column=0,padx=10,pady=10)
    text.insert(END,output)
    text.config(spacing2=1.5,state=DISABLED,height=7,width=30,font=myFont,autoseparators=2)
    
def change_nice():
    ch_Priority = my_entry1.get()
    ch_PID = my_entry2.get()
    update = "sudo renice " + ch_Priority + " -p " + ch_PID
    os.system(update)
    print(ch_Priority)
    print(ch_PID)

def update_nice():
    p=sub.Popen('./nice_display.sh',stdout=sub.PIPE, stderr=sub.PIPE)
    output,errors = p.communicate()
    text = tk.Text(root)
    text.grid_forget()
    text.grid(row=6,column=0,padx=10,pady=10)
    text.insert(END,output)
    text.config(spacing2=1.5,state=DISABLED,height=7,width=30,font=myFont,autoseparators=2)


#def updated_nice():
#    print (os.system(ps -eo pid,pri,ni | head -n 6))
org_button = tk.Button(root, anchor=CENTER,font=myFont,justify=CENTER,text="Original value", command = original_nice)
org_button.grid(row=0,column=0,padx=10,pady=10)

my_label1 = tk.Label(root, text = "Priority value")
my_label1.grid(row = 2, column = 0,padx=10,pady=10)
my_entry1 = tk.Entry(root)
my_entry1.grid(row = 2, column = 1)

my_label2 = tk.Label(root, text="PID")
my_label2.grid(row=3, column=0)
my_entry2 = tk.Entry(root)
my_entry2.grid(row=3,column=1)

my_button1 = tk.Button(root, anchor=CENTER,font=myFont,justify=CENTER, text = "Update", command = change_nice)
my_button1.grid(row = 4, column = 1)

upd_button = tk.Button(root, text="Updated value", command=update_nice,anchor=CENTER,font=myFont,justify=CENTER)
upd_button.grid(row=5, column=0)


#my_button = tk.Button(root, text = "Submit" )
#my_button.grid(row = 3, column = 0)

root.mainloop()






