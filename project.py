import tkinter
import threading 
from tkinter import messagebox
import sys



task = []
timer = threading 
real_timer = threading
ok_thread = True

def get_entry(event = " "):
    text = todo.get()
    hour = int(time.get())
    todo.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    todo.focus_set()
    add_list(text, hour)
    if 0 < hour < 999:
        update_list()
    
def add_list(text, hour):
    tasks.append([text, hour])
    timer = threading.Timer(hour, time_passed, [text])
    timer.start()

def update_list():
    if todolist.sixe() > 0:
        todolist.delete(0, "end")
    for task in tasks:
        todolist.insert("end", "[" + task[0] + "] Due Date: " + str[task[1] + " second"]
        