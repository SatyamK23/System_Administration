import tkinter as tk
import os

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,askdirectory
from pathlib import Path
from os import listdir
from os.path import isfile, join

root=tk.Tk()
root.title('File Permissions')


def add_permission():
    filename = askopenfilename()
    basename  = Path(filename).name
    filename ="ls -l "+basename
    os.system(filename)
    pervalue = my_entry1.get()
    chvalue = "chmod +" +pervalue + " "+ basename
    os.system(chvalue)
    filename ="ls -l "+basename
    os.system(filename)

def permug():
    filename = askopenfilename()
    basename  = Path(filename).name
    print ("You have selected ",usrtype.get())
    print ("Permission updation",fileper.get())
    list  = "ls -l "+basename
    os.system(list)
    if usrtype.get()=='User':
        if fileper.get()=='Read':
            chvalue = "chmod u+r" + " "+ basename
            print(chvalue)
            os.system(chvalue)
            filename = "ls -l "+basename
            os.system(filename)
        elif fileper.get()=='Write':
            chvalue ="chmod u+w"+" "+basename
            os.system(chvalue)
        else:
            chvalue="chmod u+x"+" "+basename
            os.system(chvalue)
    elif usrtype.get()=='Group':
        if fileper.get()=='Read':
            chvalue = "chmod g+r" + " "+ basename
            os.system(chvalue)
        elif fileper.get()=='Write':
            chvalue ="chmod g+w"+" "+basename
            os.system(chvalue)
        else:
            chvalue="chmod g+x"+" "+basename
            os.system(chvalue)
    elif usrtype.get()=='Other':
        if fileper.get()=='Read':
            chvalue = "chmod o+r" + " "+ basename
        elif fileper.get()=='Write':
            chvalue ="chmod o+w" +" "+basename
        else:
            chvalue="chmod o+x" +" "+basename
    else:
        if fileper.get()=='Read':
            chvalue="chmod a+r"+" "+basename
        elif fileper.get()=='Write':
            chvalue ="chmod a+w"+" "+basename
        else:
            chvalue="chmod a+x" +" "+basename
    list  = "ls -l "+basename
    os.system(list)

def delete_permission():
    filename = askopenfilename()
    basename  = Path(filename).name
    pervalue = my_entry2.get()
    if pervalue =='':
        messagebox.showerror("error", "insert value")
    else:
        filename ="ls -l "+basename
        os.system(filename)
        chvalue = "chmod -" +pervalue + " "+ basename
        os.system(chvalue)
    #filename ="ls -l "+basename
    #os.system(filename)

'''
Function of converting umask value into file permision of files
User enters umask value of particular file to get default file permission of that directory.
'''
def umaskperfiles():
    filename = askopenfilename()
    basename  = Path(filename).name
    umask_value = my_entry3.get()
    if umask_value =='':
        messagebox.showerror("error", "insert value from 000 to 666")
    else:
        if os.path.isfile(filename):
            default_value = 666 - int(umask_value)
            messagebox.showinfo("File name",filename)
            messagebox.showinfo(title="fILE umask", message=["Value of Umask for directory",default_value],icon="info")

'''
Function of converting umask value  into file permision of directory
User enters umask value of particular directoryto get default file permission of that directory.
'''
def umaskperdir():
    filename = askopenfilename()
    basename  = Path(filename).name
    umask_value = my_entry4.get()
    if umask_value =='':
        messagebox.showerror("error", "insert value from 000 to 777")
    else:
        dirname = askdirectory()
        if os.path.isdir(os.getcwd()):
            default_value = 777 - int(umask_value)
            messagebox.showinfo("File path",os.getcwd())
            messagebox.showinfo(title="Directory umask", message=["Value of Umask for directory",default_value],icon="info")

def acl():
    filename = askopenfilename()
    basename  = Path(filename).name
    if usrtype.get()=='User' and opt.get()=='Add':
        usrname = my_entry5.get()
        aclper = "setfacl -m u:"+usrname+":rw-"+" "+basename
        print (aclper)
        os.system(aclper)
    elif usrtype.get()=='Group' and opt.get()=='Add':
        grpname = my_entry5.get()
        aclper = "setfacl -m g:"+grpname+":rw-"+" "+basename
        print (aclper)
        os.system(aclper)
    elif usrtype.get()=='User' and opt.get()=='Delete':
        usrname = my_entry5.get()
        aclper = "setfacl -x u:"+usrname+" "+basename
        os.system(aclper)
    else:
        grpname = my_entry5.get()
        aclper = "setfacl -x g:"+grpname+" "+basename
        os.system(aclper)


    list  = "ls -l "+basename
    os.system(list)


my_label1 = tk.Label(root, text = "change file permission ")
my_label1.grid(row = 1, column = 0,padx=10, pady=10)
my_entry1 = tk.Entry(root)
my_entry1.grid(row=1,column=1,padx=10,pady=10)
my_button = tk.Button(root, text = "Add Permission", command = add_permission)
my_button.grid(row = 1, column = 2,padx=10, pady=10)

my_label = tk.Label(root, text = "Delete File Permission ")
my_label.grid(row = 2, column = 0,padx=10, pady=10)
my_entry2 = tk.Entry(root)
my_entry2.grid(row = 2, column = 1,padx=3, pady=3)
my_button = tk.Button(root, text = "Delete Permission", command = delete_permission)
my_button.grid(row = 2, column = 2,padx=10, pady=10)

my_label = tk.Label(root, text = "Mask Value for files ")
my_label.grid(row = 3, column = 0,padx=10, pady=10)
my_entry3 = tk.Entry(root)
my_entry3.grid(row =3 , column = 1,padx=3, pady=3)
my_button = tk.Button(root, text = "Umask for files", command = umaskperfiles)
my_button.grid(row = 3, column = 2,padx=10, pady=10)

my_label = tk.Label(root, text = "Mask Value for Directory")
my_label.grid(row = 4, column = 0,padx=10, pady=10)
my_entry4 = tk.Entry(root)
my_entry4.grid(row =4 , column = 1,padx=3, pady=3)
my_button = tk.Button(root, text = "Umask for Directory", command = umaskperdir)
my_button.grid(row = 4, column = 2,padx=10, pady=10)

my_label5 = tk.Label(root, text="Permission of Users or Group")
my_label5.grid(row = 5, column = 0,padx=3, pady=3)

usrtype = StringVar(root)
usrtype.set("User") #default value
ust = tk.OptionMenu(root, usrtype, "User", "Group", "Other","All")
ust.grid(row=5,column=1,padx=10,pady=10)    

fileper = StringVar(root)
fileper.set("Read")
w = tk.OptionMenu(root, fileper, "Read","Write","Execute")
w.grid(row=5,column=2,padx=10,pady=10)
my_button = tk.Button(root, text="Change Permission",command = permug)
my_button.grid(row=6,column=1,padx=10,pady=10)

my_label = tk.Label(root, text="Access Control List")
my_label.grid(row = 7,column=0,padx=10,pady=10)
usert = tk.OptionMenu(root, usrtype, "User", "Group")
usert.grid(row=7,column=1,padx=10,pady=10)   
opt = StringVar(root)
opt.set("Add")
optchg = tk.OptionMenu(root, opt,"Add","Delete")
optchg.grid(row=7,column=2,padx=10,pady=10)
my_entry5 = tk.Entry(root)
my_entry5.grid(row=7,column=3,padx=10,pady=10)
my_button = tk.Button(root, text="Access Control List",command= acl)
my_button.grid(row=8,column=1,padx=10,pady=10)

quit_button = tk.Button(root, command=root.quit, text="Cancel")
quit_button.grid(row=9,column=1,padx=10,pady=10)

root.mainloop()
