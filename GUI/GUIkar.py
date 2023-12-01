import tkinter as tk
from tkinter import messagebox

master = tk.Tk()

def add():
    try:
        x = int(num1.get())
        y = int(num2.get())
        result = x + y
        messagebox.config(state="normal")
        messagebox.delete("1.0", "end")  # Clear previous result
        messagebox.insert("1.0", f" {result}")
        messagebox.config(state="disabled")
    except:
        messagebox.showerror("Error!", "The value is invalid")

label1 = tk.Label(master, text="Enter the number 1:")
label2 = tk.Label(master, text="Enter the number 2")
num1 = tk.Entry(master)
num2 = tk.Entry(master)
Button1 = tk.Button(master, text="Add", padx=40, pady=20, command=add)
Button2 = tk.Button(master, text="Exit", padx=40, pady=20, command=master.quit)
messagebox = tk.Text(master,height=2,width=10,state="disabled")




label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
num1.grid(row=0, column=1, ipadx=20, ipady=15)
num2.grid(row=1, column=1, ipadx=20, ipady=15)
Button1.grid(row=3, column=0, columnspan=2)
Button2.grid(row=4, column=0, columnspan=2)
messagebox.grid(row=4, column=0, columnspan=2)


master.mainloop()
