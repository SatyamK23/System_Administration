import tkinter as tk
import subprocess as sub
import matplotlib.pyplot as plt
import os 

from tkinter import *
root = tk.Tk()
root.title('CPU Usage')

#user_cpu_per = [(0.5 ,1),
#(0.6,1),
#(1.1,2),
#(4.1,1),
#(0.9,1),
#(3.8, 1),
#(2.1, 1),
#(0.0 ,214),
#(0.1,3),
#(0.2,1),
#(0.3,1)]
#sizes, labels = [i[1] for i in user_cpu_per],[i[0] for i in user_cpu_per]
#plt.pie(sizes, labels=labels,autopct='%1.1i%%')
#plt.show()

def refresh_cpu_usage():
    os.system('./cpu_col.sh')

my_label = tk.Label(root, text= "CPU Usage")
my_label.grid(row=1,column =0,padx=10,pady=10)
upd_btn = tk.Button(root, text="Refresh", command = refresh_cpu_usage)
upd_btn.grid(row=1,column=1,padx=10,pady=10)
root.mainloop()
