import tkinter as tk
import subprocess as sub
import matplotlib.pyplot as plt
import os 

from tkinter import *
root = tk.Tk()
root.title('CPU Usage')

def cpu_pie_chart():
    cpu_usage_plot = "ps aux | awk 'NR>2{arr[$1]+=$3}END{for(i in arr) print i,arr[i]}' > cpu.txt"
    os.system(cpu_usage_plot)
    file_path = os.getcwd()
    print("Plotting CPU Usage")
    file_name = os.path.join(file_path,'cpu.txt')
    open_file = open(file_name,"r")
    plot_data(open_file)
    print ("CPU Usage Plotted")


def mem_pie_chart():
    memory_usage_plot = "ps aux | awk 'NR>2{arr[$1]+=$6}END{for(i in arr) print i,arr[i]/1024}' > memory.txt"
    os.system(memory_usage_plot)
    file_path = os.getcwd()
    print("Plotting Memory Usage")
    plot_data(open(os.path.join(file_path, 'memory.txt'), 'r'))
    print ("Plotted Memory Usage Pie Chart")

def plot_data(data):
    dat_list = {}

    for i in data.readlines():
        split_list = i.split()
        dat_list[split_list[0]] = split_list[1]
        print (dat_list)

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

    plt.pie(dat_list.values(), labels=dat_list.keys(), colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

my_label = tk.Label(root, text= "CPU Usage")
my_label.grid(row=1,column =0,padx=10,pady=10)
upd_btn = tk.Button(root, text="Refresh", command = cpu_pie_chart)
upd_btn.grid(row=1,column=1,padx=10,pady=10)

my_label = tk.Label(root, text= "Memory Usage")
my_label.grid(row=2,column =0,padx=10,pady=10)
upd_btn = tk.Button(root, text="Refresh", command = mem_pie_chart)
upd_btn.grid(row=2,column=1,padx=10,pady=10)
root.mainloop()
