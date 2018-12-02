import tkinter as tk
import subprocess as sub
import matplotlib.pyplot as plt
import os, csv
import pandas as pd

from tkinter import *
root = tk.Tk()
root.title('CPU Usage')

def cpu_usage():
    os.system('./cpu_col.sh')
    df = pd.read_csv('cpu.csv')
    col = pd.DataFrame(columns=['users','usage'])
    split = df.ix[:,0].str.split(" ")
    col.ix[:,0] = split.str[0]
    col.ix[:,1] = split.str[-1]
    user_data = col.ix[:,0]
    usage_data = col.ix[:,1]
    plt.pie(usage_data, autopct='%1.1f%%', startangle=120)
    plt.legend(labels = user_data)
    plt.show()
    os.system('rm cpu.csv')

def mem_usage():
    os.system('./mem_usage.sh')
    df = pd.read_csv('mem_usage.csv')
    col = pd.DataFrame(columns=['users','usage'])
    split = df.ix[:,0].str.split(" ")
    col.ix[:,0] = split.str[0]
    col.ix[:,1] = split.str[-1]
    user_data = col.ix[:,0]
    usage_data = col.ix[:,1]
    plt.pie(usage_data, autopct='%1.1f%%', startangle=120)
    plt.legend(labels = user_data)
    plt.show()
    os.system('rm mem_usage.csv')
  #  display()
  #  os.system('truncate -s 0 mem_usage.csv')

my_label = tk.Label(root, text= "CPU Usage")
my_label.grid(row=1,column =0,padx=10,pady=10)
upd_btn = tk.Button(root, text="Refresh CPU Usage", command = cpu_usage)
upd_btn.grid(row=1,column=1,padx=10,pady=10)
my_label = tk.Label(root, text= "Memory Usage")
my_label.grid(row=2,column =0,padx=10,pady=10)
upd_btn = tk.Button(root, text="Refresh Memory Usage", command = mem_usage)
upd_btn.grid(row=2,column=1,padx=10,pady=10)
root.mainloop()
