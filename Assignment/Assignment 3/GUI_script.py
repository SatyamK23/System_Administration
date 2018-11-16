import tkinter as tk
import subprocess as sub
import os

from subprocess import call
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter.ttk import *

root=tk.Tk()
root.title("GRUB Customizer")
WINDOW_SIZE="600x400"


def GRUB_timeout():
  #  change_window()
    grub_timeout = my_entry.get()
    upd = './update.sh ' + grub_timeout
    os.system(upd)
    os.system('less /etc/default/grub')

def GRUB_default():
    change_window()
    grub_def = my_entry1.get()
    upd = './default.sh ' + grub_def
    os.system(upd)
    os.system('less /etc/default/grub')

#def Bootsplash():
#    filename = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) 
#    print(filename)
#    return filename

aWindow = tk.Toplevel(root)
def try_login():
    if password_guess.get() != "":
        messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
        change_window()
    else:
        messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")


def change_window():
    aWindow.destroy()

    root.iconify()
    root.deiconify()

def automaticshutdown():
    os.system('shutdown -P now')

def automaticrestart():
    os.system('shutdown -r now')

#Creating password entry boxes
root.withdraw()
password_text = tk.Label(root, text="Password:")
password_text.grid(row=1,column=2,padx=10, pady=10)
password_guess = tk.Entry(root, show="*")
password_guess.grid(row=1,column=3,padx=10,pady=10)
passwd_btn = tk.Button(root, text="Login",command=try_login)
passwd_btn.grid(row=3,column=3,padx=10,pady=10)
cancel_btn = tk.Button(root, text="Cancel",command=root.quit)
cancel_btn.grid(row=3,column=4,padx=10,pady=10)

#tk.Label(root, text="This is the Window of User Management")
my_label = tk.Label(aWindow, text = "Grub Timeout")
my_label.grid(row = 0, column = 0,padx=10, pady=10)
my_entry = tk.Entry(aWindow)
my_entry.grid(row = 0, column = 1,padx=3, pady=3)
my_button = tk.Button(aWindow, text = "Grub Timeout", command =GRUB_timeout )
my_button.grid(row = 0, column = 2,padx=10, pady=10)

my_label1 = tk.Label(aWindow, text = "Grub Default")
my_label1.grid(row = 1, column = 0,padx=10, pady=10)
my_entry1 = tk.Entry(aWindow)
my_entry1.grid(row = 1, column = 1,padx=3, pady=3)

defbtn = tk.Button(aWindow, text="Grub Default", command=GRUB_default)
defbtn.grid(row=1,column=2, padx=10,pady=10)


#my_label2 = tk.Label(root, text = "Bootsplash")
#my_label2.grid(row = 2, column = 0,padx=10, pady=10)
#splash_file =tk.Button(root, text="Choose File", command=Bootsplash).grid(row=2,column=1,padx=10,pady=10)
#root.geometry(WINDOW_SIZE)


my_label3 = tk.Label(aWindow, text = "Automatic Reboot")
my_label3.grid(row = 2, column = 0,padx=10, pady=10)
tk.Button(aWindow, text="Automatic Reboot", command=automaticrestart).grid(row=2,column=1, padx=10,pady=10)

my_label4 = tk.Label(aWindow, text = "Automatic Shutdown")
my_label4.grid(row = 3, column = 0,padx=10, pady=10)
tk.Button(aWindow, text="Automatic Shutdown", command= automaticshutdown).grid(row=3,column=1,padx=10,pady=10)
root.mainloop()

