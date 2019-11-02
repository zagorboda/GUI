from tkinter import *
from datetime import datetime

root = Tk()
root.title("Timer")

temp = 0
after_id = ''


def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.utcfromtimestamp(temp).strftime("%M:%S")
    time_lbl.configure(text=str(f_temp))
    temp += 1


def start():
    btn_start.grid_forget()
    btn_stop.grid(row=1, columnspan=2, sticky="ew")
    tick()


def stop():
    btn_stop.grid_forget()
    btn_continue.grid(row=1, column=0, sticky="ew")
    btn_reset.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)


def f_continue():
    btn_continue.grid_forget()
    btn_reset.grid_forget()
    btn_stop.grid(row=1, columnspan=2, sticky="ew")
    tick()


def reset():
    global temp
    temp = 0
    time_lbl.configure(text="00:00")
    btn_continue.grid_forget()
    btn_reset.grid_forget()
    btn_start.grid(row=1, columnspan=2, sticky="ew")


time_lbl = Label(root, width=5, font=("Ubuntu", 100), text="00:00")
time_lbl.grid(row=0, columnspan=2)

btn_start = Button(root, text="Start", font=("Ubuntu", 30), command=start)
btn_stop = Button(root, text="Stop", font=("Ubuntu", 30), command=stop)
btn_continue = Button(root, text="Continue", font=("Ubuntu", 30), command=f_continue)
btn_reset = Button(root, text="Reset", font=("Ubuntu", 30), command=reset)

btn_start.grid(row=1, columnspan=2, sticky="ew")

root.mainloop()
