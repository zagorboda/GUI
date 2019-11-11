from tkinter import *
import numpy as np
from tkinter.messagebox import *

# TODO
#  resize labels in x or y if number longer than that label
#  firstly show empty warning , then non digit
#  add top menu that include links to main page and all functions
#  input matrix shape: if empty_input warning shown don't show non digit warning

root = Tk()
root.title("Matrix Calculator")

btn_start_det = Button(root, text="Matrix determinant", command=lambda: Determinant(root))
btn_start_det.grid(row=0, column=0)
btn_start_rank = Button(root, text="Matrix rank", command=lambda: Rank(root))
btn_start_rank.grid(row=0, column=1)
btn_start_sum = Button(root, text="Matrix sum", command=lambda: MatrixSum(root))
btn_start_sum.grid(row=1, column=0)


class Determinant:

    def __init__(self, main):
        btn_start_det.grid_forget()
        btn_start_rank.grid_forget()
        btn_start_sum.grid_forget()
        self.entry_m = Entry(root)
        self.entry_n = Entry(root)
        self.label_entry_m = Label(root, text="Enter m:")
        self.label_entry_n = Label(root, text="Enter n:")
        self.label_entry_m.grid(row=0, column=0)
        self.label_entry_n.grid(row=1, column=0)
        self.entry_m.grid(row=0, column=1)
        self.entry_n.grid(row=1, column=1)
        self.btn_start = Button(root, text="Start", command=lambda: self.check())
        self.btn_start.grid(row=3, column=0)

    def check(self):
        show_empty_input = False
        show_non_digit_input = False
        m_correct_input = 0
        n_correct_input = 0
        global m
        m = self.entry_m.get()
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
                if show_non_digit_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        global n
        n = self.entry_n.get()
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
                if show_non_digit_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        try:
            if int(n) != int(m):
                showwarning("Warning", "To calculate determinate number of rows must be equal to number of columns")
        except ValueError:
            pass

        if m_correct_input == 2 and n_correct_input == 2 and n == m:
            self.entry_m.grid_forget()
            self.entry_n.grid_forget()
            self.btn_start.grid_forget()
            self.label_entry_n.grid_forget()
            self.label_entry_m.grid_forget()
            self.show()

    def show(self):
        a = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                entry = Entry(root, width=10)
                entry.grid(row=i, column=j)
                a[i][j] = entry
        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(m, n, a))
        btn1.grid(row=i + 1, column=0, columnspan=3)

    def calculate(self, m, n, a):
        c = []
        show_empty_input = False
        show_non_digit_input = False
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
                    except ValueError:
                        if show_non_digit_input == False:
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True

        if len(c) == m*n:
            np.array(c)
            c = np.reshape(c, (m, n))
            lbl1 = Label(root, text="Matrix determinant = %.4f" % np.linalg.det(c))
            lbl1.grid(row=i + 2, column=0, columnspan=3)


class Rank:

    def __init__(self, main):
        btn_start_det.grid_forget()
        btn_start_rank.grid_forget()
        btn_start_sum.grid_forget()
        self.entry_m = Entry(root)
        self.entry_n = Entry(root)
        self.label_entry_m = Label(root, text="Enter m:")
        self.label_entry_n = Label(root, text="Enter n:")
        self.label_entry_m.grid(row=0, column=0)
        self.label_entry_n.grid(row=1, column=0)
        self.entry_m.grid(row=0, column=1)
        self.entry_n.grid(row=1, column=1)
        self.btn_start = Button(root, text="Start", command=lambda: self.check())
        self.btn_start.grid(row=3, column=0)

    def check(self):
        show_empty_input = False
        show_non_digit_input = False
        m_correct_input = 0
        n_correct_input = 0
        global m
        m = self.entry_m.get()
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
                if show_non_digit_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        global n
        n = self.entry_n.get()
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
                if show_non_digit_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        if m_correct_input == 2 and n_correct_input == 2 and n == m:
            self.entry_m.grid_forget()
            self.entry_n.grid_forget()
            self.btn_start.grid_forget()
            self.label_entry_n.grid_forget()
            self.label_entry_m.grid_forget()
            self.show()

    def show(self):
        a = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                entry = Entry(root, width=10)
                entry.grid(row=i, column=j)
                a[i][j] = entry
        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(m, n, a))
        btn1.grid(row=i + 1, column=0, columnspan=3)

    def calculate(self, m, n, a):
        c = []
        show_empty_input = False
        show_non_digit_input = False
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
                    except ValueError:
                        if show_non_digit_input == False:
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True
        np.array(c)
        c = np.reshape(c, (m, n))
        lbl1 = Label(root, text="Matrix rank = %.4f" % np.linalg.matrix_rank(c))
        lbl1.grid(row=i + 2, column=0, columnspan=3)


class MatrixSum:

    def __init__(self, main):
        btn_start_det.grid_forget()
        btn_start_rank.grid_forget()
        btn_start_sum.grid_forget()
        self.entry_m = Entry(root)
        self.entry_n = Entry(root)
        self.label_entry_m = Label(root, text="Enter m:")
        self.label_entry_n = Label(root, text="Enter n:")
        self.label_entry_m.grid(row=0, column=0)
        self.label_entry_n.grid(row=1, column=0)
        self.entry_m.grid(row=0, column=1)
        self.entry_n.grid(row=1, column=1)
        self.btn_start = Button(root, text="Start", command=lambda: self.check())
        self.btn_start.grid(row=3, column=0)

    def check(self):
        show_empty_input = False
        show_non_digit_input = False
        m_correct_input = 0
        n_correct_input = 0
        global m
        m = self.entry_m.get()
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
                if show_non_digit_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        global n
        n = self.entry_n.get()
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
                if show_non_digit_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        if m_correct_input == 2 and n_correct_input == 2 and n == m:
            self.entry_m.grid_forget()
            self.entry_n.grid_forget()
            self.btn_start.grid_forget()
            self.label_entry_n.grid_forget()
            self.label_entry_m.grid_forget()
            self.show()

    def show(self):
        a = [[0 for x in range(n)] for y in range(m)]
        c = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                entry1 = Entry(root, width=10)
                entry1.grid(row=i, column=j)
                label_empty = Label(root, width=5)
                label_empty.grid(row=i, column=n+1)
                entry2 = Entry(root, width=10)
                entry2.grid(row=i, column=n+j+2)
                a[i][j] = entry1
                c[i][j] = entry2
        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(m, n, a, c))
        btn1.grid(row=i + 1, column=0, columnspan=3)

    def calculate(self, m, n, a, c):
        show_empty_input = False
        show_non_digit_input = False
        b = [[0 for x in range(n)] for y in range(m)]
        d = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                b[i][j] = a[i][j].get()
                d[i][j] = c[i][j].get()
                if (b[i][j] == "") & (d[i][j] == "") & (show_empty_input == False):
                    showwarning("Warning", "You have empty input")
                    show_empty_input = True
                else:
                    try:
                        b[i][j] = int(a[i][j].get())
                        d[i][j] = int(c[i][j].get())
                    except ValueError:
                        if show_non_digit_input == False:
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True
        for i in range(m):
            for j in range(n):
                label = Label(root, width=3, text=b[i][j] + d[i][j])
                label.grid(row=i+m+1, column=j)


root.mainloop()
