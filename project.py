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

# widgets
    label = tkinter.Label(app, text="Enter work to do", wraplength = 200, justify = tkinter.LEFT)
    label_hour = tkinter.Label(app, text="Enter time", wraplength = 250, justify = tkinter.LEFT)
    todo = tkinter.Entry(app, width = 60)
    time = tkinter.Entry(app, width = 60)
    send = tkinter.Button(app, text='Add task', fg="#ffffff", bg='#6186AC', height=3, width=30, command=get_entry)
    quit = tkinter.Button(app, text='Exit', fg="#ffffff", bg='#EB6464', height=3, width=30, command=app.destroy)
    todolist = tkinter.Listbox(app)
    if tasks != "":
        real_time()
