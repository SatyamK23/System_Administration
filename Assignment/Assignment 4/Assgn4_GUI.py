import tkinter as tk
import os  
import subprocess as sub

from tkinter import *
from tkinter.filedialog import askopenfilename


root = tk.Tk()
root.title('Assignment 4')

def add_user():
    user_name = my_entry.get()
    print(user_name)
#    user_name = "sudo useradd "+ user_name
    userid = my_entry1.get()
    #print (userid)
    userid = "sudo useradd -u "+ userid +" "+ user_name
   # print (userid)

    login_shell = my_entry2.get()
    login_shell = "sudo useradd -s "+login_shell+" "+user_name
    os.system(user_name)
    os.system(userid)
    os.system(login_shell)
    #print(login_shell)
    os.system('less >5 /etc/passwd')

#    out =  sub.Popen(["cat /etc/passwd"], stdout=sub.PIPE)
#    print (out)

def del_user():
    user_name = my_entry.get()
   # print(user_name)
    user_name = "sudo userdel "+ user_name
    os.system(user_name)
    os.system('less  /etc/passwd')

def group_Add():
    group_name = my_entry3.get()
    print(group_name)
#    group_name = "sudo groupadd "+ group_name
    groupid = my_entry4.get()
   # print (groupid)
    groupid = "sudo groupadd -g "+ groupid +" "+ group_name
   # print (groupid)
    os.system(group_name)
    os.system(groupid)
    os.system('less >5 /etc/group')

def del_group():
    group_name = my_entry3.get()
    #print(user_name)
    group_name = "sudo groupdel "+ group_name
    os.system(group_name)
    os.system('less >5 /etc/passwd')
    return group_name

def batch_add():
#    os.system('sudo -i')
    filename = askopenfilename(initialdir = "/",title="Select file")
    print(filename)
    filename = "sudo newusers "+ filename
    os.system(filename)
    return filename

menubar = tk.Menu(root)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Add User", command=add_user)
#filemenu.add_command(label="Delete User", command=del_user)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)

#For adding home directory of users
my_label = tk.Label(root, text = "UserName ")
my_label.grid(row = 0, column = 0,padx=10, pady=10)
my_entry = tk.Entry(root)
my_entry.grid(row = 0, column = 1,padx=3, pady=3)

#For taking input of UID
my_label1 = tk.Label(root, text="UID ")
my_label1.grid(row = 1, column = 0,padx=10, pady=10)
my_entry1 = tk.Entry(root)
my_entry1.grid(row =1,column=1)

#For giving path of shell
my_label2 = tk.Label(root, text="Shell:")
my_label2.grid(row = 2, column = 0,padx=10, pady=10)
my_entry2 = tk.Entry(root)
my_entry2.grid(row =2,column=1,padx=3, pady=3)

my_button = tk.Button(root, text = "Add User", command = add_user)
my_button.grid(row = 3, column = 0,padx=10, pady=10)
my_button = tk.Button(root, text = "Delete User", command = del_user)
my_button.grid(row = 3, column = 1,padx=3, pady=3)


my_label3 = tk.Label(root, text="Group Name:")
my_label3.grid(row = 4, column = 0,padx=10, pady=10)
my_entry3 = tk.Entry(root)
my_entry3.grid(row =4,column=1,padx=10, pady=10)


my_label4 = tk.Label(root, text="GroupID:")
my_label4.grid(row = 5, column = 0,padx=10, pady=10)
my_entry4 = tk.Entry(root)
my_entry4.grid(row =5,column=1,padx=3, pady=1)

my_button = tk.Button(root, text = "Add Group", command = group_Add)
my_button.grid(row = 6, column = 0,padx=3, pady=3)
my_button =tk.Button(root, text="Delete Group", command = del_group)
my_button.grid(row=6,column=1,padx=3, pady=3)

my_label5 = tk.Label(root, text="Batch Add")
my_label5.grid(row = 7, column = 0,padx=10, pady=10)
my_button = tk.Button(root, text="Choose File", command=batch_add)
my_button.grid(row=7,column=1,padx=10,pady=10)

root.mainloop()



