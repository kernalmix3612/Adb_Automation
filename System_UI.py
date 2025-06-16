from datetime import *
from sched import scheduler
from tkinter import Button, messagebox
import pandas as pd
from pandas import *
import tkinter as tk
import time
import schedule
from pathlib import Path


window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
open_file=tk.Button()
window.mainloop()