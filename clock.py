import tkinter as tk
from time import strftime

def time():
    
    string = strftime('%I:%M:%S %p')  
   
    lbl.config(text = string)
   
    lbl.after(1000, time)

root = tk.Tk()
root.title('My First Digital Clock')
lbl = tk.Label(root, font = ('French Script MT', 100),
            background = '#060337',
            foreground = 'cyan')
lbl.pack(anchor = 'center')
time()
root.mainloop()
