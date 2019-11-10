from tkinter import *
import numpy as np
from tkinter.messagebox import *

# TODO
#  resize labels in x or y if number longer than that label
#  firstly show empty warning , then non digit
#  for determinant check if m == n
#  add top menu that include links to main page and all functions
#  input matrix shape: if empty_input warning shown dot show non digit warning

root = Tk()
root.title("Matrix Calculator")


# c = []
# d = []
# b = [[0 for x in range(2)] for y in range(2)]

show_empty_input = False
show_nondigit_input = False


btn_start_det = Button(root, text="Matrix determinant", command=lambda: det_start_screen())
btn_start_det.grid(row=0, column=0)


def det_start_screen():
    btn_start_det.grid_forget()
    label_entry_m = Label(root, text="Enter m:")
    label_entry_m.grid(row=0, column=0)
    label_entry_n = Label(root, text="Enter n:")
    label_entry_n.grid(row=1, column=0)
    entry_m = Entry(root)
    entry_m.grid(row=0, column=1)
    entry_n = Entry(root)
    entry_n.grid(row=1, column=1)
    btn_start = Button(root, text="Start", command=lambda: check(entry_m, entry_n, btn_start, label_entry_n, label_entry_m))
    btn_start.grid(row=3, column=0)


def check(entry_m, entry_n, btn_start, label_entry_n, label_entry_m):
    show_empty_input = False
    show_nondigit_input = False
    m_correct_input = 0
    n_correct_input = 0
    global m
    m = entry_m.get()
    if (m == "") & (show_empty_input == False):
        showwarning("Warning", "You have empty input")
        show_empty_input = True
    else:
        try:
            m = int(m)
            m_correct_input += 1
            if m > 0:
                m_correct_input += 1

        except ValueError:
            if show_nondigit_input == False:
                showwarning("Warning", "Your input include non digit symbols")
                show_nondigit_input = True

    global n
    n = entry_n.get()
    if (n == "") & (show_empty_input == False):
        showwarning("Warning", "You have empty input")
        show_empty_input = True
    else:
        try:
            n = int(n)
            n_correct_input += 1
            if n > 0:
                n_correct_input += 1
        except ValueError:
            if show_nondigit_input == False:
                showwarning("Warning", "Your input include non digit symbols")
                show_nondigit_input = True

    try:
        if int(n) != int(m):
            showwarning("Warning", "To calculate determinate number of rows must be equal to number of columns")
    except ValueError:
        pass

    if m_correct_input == 2 and n_correct_input == 2 and n == m:
        entry_m.grid_forget()
        entry_n.grid_forget()
        btn_start.grid_forget()
        label_entry_n.grid_forget()
        label_entry_m.grid_forget()
        show()


def show():
    a = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        for j in range(n):
            entry = Entry(root, width=10)
            entry.grid(row=i, column=j)
            a[i][j] = entry
    btn1 = Button(root, text="Button", command=lambda: calculate(m, n, a))
    btn1.grid(row=i + 1, column=0, columnspan=3)


def calculate(m, n, a):
    c = []
    d = []
    global show_empty_input, show_nondigit_input
    show_empty_input = False
    show_nondigit_input = False
    b = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[i][j].get()
            if (b[i][j] == "") & (show_empty_input == False):
                showwarning("Warning", "You have empty input")
                show_empty_input = True
            else:
                try:
                    b[i][j] = int(a[i][j].get())
                    c.append(b[i][j])
                    print(b[i][j])
                except ValueError:
                    if(show_nondigit_input == False):
                        showwarning("Warning", "Your input include non digit symbols")
                        show_nondigit_input = True
    d = c
    np.array(d)
    d = np.reshape(d, (m, n))
    print(d)
    print("%.6f" % np.linalg.det(d))
    lbl1 = Label(root, text="Matrix determinant = %f" % np.linalg.det(d))
    lbl1.grid(row=i + 1, column=0, columnspan=3)

# entry1 = Entry(root)
# entry1.grid(row=0, column=0)
#
#
# btn1 = Button(root, text="Button", command=lambda: calculate())
# btn1.grid(row=0, column=1)
#
# lbl1 = Label(root)
# lbl1.grid(row=0, column=2)


# a = [[0 for x in range(2)] for y in range(2)]
#
# for i in range(m):
#     for j in range(n):
#         entry = Entry(root, width=10)
#         entry.grid(row=i, column=j)
#         a[i][j] = entry

# command=lambda: calculate()
# btn1 = Button(root, text="Button", command=lambda: calculate())
# btn1.grid(row=4, column=0, columnspan=3)

# lbl1 = Label(root, text="Matrix determinant = ")
# lbl1.grid(row=5, column=0, columnspan=3)

root.mainloop()
