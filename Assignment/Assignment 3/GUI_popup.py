from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
import subprocess as sub
#username = ("Satyam")
password = ("")


def try_login():
    if password_guess.get() != "":
        messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
    else:
        messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
        

#Gui Things
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("Log-In")
window.geometry("200x150")

#Creating the password entry boxes
password_text = Label(window, text="Password:")
password_guess = Entry(window, show="*")

#attempt to login button
attempt_login = Button(window, text="Login", command=try_login)
cancel_btn = Button(text="Cancel",command=window.quit)
password_text.pack()
password_guess.pack()
attempt_login.pack()
cancel_btn.pack()

#Main Starter
window.mainloop()
