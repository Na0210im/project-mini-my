import tkinter
import threading 
from tkinter import messagebox
import sys
import time as tm


task = []
timer = threading 
real_timer = threading
ok_thread = true

def get_entry(event = " "):
    text = todo.get()
    hour = int(time.get())
    todo.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    todo.focus_set()
    add_list(text, hour)
    if 0 < hour < 999:
        update_list()