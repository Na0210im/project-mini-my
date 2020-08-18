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

def time_passed(task):
    tkinter.messagebox.showinfo("Reminder", "Time for: " + task)

def real_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)
        task[1] -= 1
    update_list()

if __name__ == '__main__':
    app = tkinter.Tk()
    app.geometry("480x680")
    app.title("Student To Do List")
    app.rowconfigure(0, weight = 1)

    frame = tkinter.Frame(app)
    frame.pack()