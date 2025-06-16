import tkinter
from tkinter import *
from tkinter.ttk import * 
from tkinter.filedialog import askopenfile, asksaveasfilename
Tui = tkinter.Tk()
Tui.geometry('720x480')
button = tkinter.Button(Tui,fg="blue", text='Setting', width=25)
filling = tkinter.Entry(fg="green", width=50)
filling_name = filling.get()
Tui.title('System UI')
button.pack()
filling.pack()
filling_name
Tui.mainloop()