from tkinter import *
import numpy as np
from tkinter.messagebox import *

# TODO : resize labels in x or y if number longer than that label; firstly show empty warning , then non digit;

root = Tk()
root.title("Matrix Calculator")

m, n = 2, 2
c = []
d = []
b = [[0 for x in range(2)] for y in range(2)]

show_empty_input = False
show_nondigit_input = False


def calculate():
    global c,d
    global show_empty_input, show_nondigit_input
    show_empty_input = False
    show_nondigit_input = False
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
    d = np.reshape(d, (2, 2))
    print(d)
    print("%.6f" % np.linalg.det(d))
    lbl1.configure(text="Matrix determinant = %f" % np.linalg.det(d))

# entry1 = Entry(root)
# entry1.grid(row=0, column=0)
#
#
# btn1 = Button(root, text="Button", command=lambda: calculate())
# btn1.grid(row=0, column=1)
#
# lbl1 = Label(root)
# lbl1.grid(row=0, column=2)


a = [[0 for x in range(2)] for y in range(2)]

for i in range(m):
    for j in range(n):
        entry = Entry(root, width=10)
        entry.grid(row=i, column=j)
        a[i][j] = entry

# command=lambda: calculate()
btn1 = Button(root, text="Button", command=lambda: calculate())
btn1.grid(row=4, column=0, columnspan=3)

lbl1 = Label(root, text="Matrix determinant = ")
lbl1.grid(row=5, column=0, columnspan=3)

root.mainloop()
