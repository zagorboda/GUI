from tkinter import *
import numpy as np
from tkinter.messagebox import *

# TODO
#  resize labels in x or y if number longer than that label
#  add scroll for big matrix
#  add exception to linalg singular matrix
#  fix exception warning in matrix's value input

root = Tk()
# root.grid_columnconfigure(0, weight=1)

# numpy.linalg.linalg.LinAlgError: Last 2 dimensions of the array must be square
# numpy.linalg.linalg.LinAlgError: Singular matrix

class MainScreen:

    def __init__(self):

        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        for item in _list:
            item.grid_forget()

        root.title("Matrix Calculator")

        self.btn_start_det = Button(root, width=15, text="Matrix determinant", command=lambda: Determinant(),
                                    bg='#dccdc7')
        self.btn_start_det.grid(row=0, column=0, padx=5, pady=5)
        self.btn_start_rank = Button(root, width=15, text="Matrix rank", command=lambda: Rank(), bg='#dccdc7')
        self.btn_start_rank.grid(row=0, column=1, padx=5, pady=5)
        self.btn_start_sum = Button(root, width=15, text="Matrix sum", command=lambda: MatrixSum(), bg='#dccdc7')
        self.btn_start_sum.grid(row=1, column=0, padx=5, pady=5)
        self.btn_start_sum = Button(root, width=15, text="Matrix multiplication", command=lambda: MatrixMultiplication()
                                    , bg='#dccdc7')
        self.btn_start_eq = Button(root, width=15, text="Matrix Equation", command=lambda: MatrixEquation(),
                                   bg='#dccdc7')
        self.btn_start_eq.grid(row=2, column=0, padx=5, pady=5)
        self.btn_start_sum.grid(row=1, column=1, padx=5, pady=5)


class Determinant:

    def __init__(self):
        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        for item in _list:
            item.grid_forget()

        root.title("Matrix Determinant")

        self.entry_m = Entry(root)
        self.entry_n = Entry(root)
        self.label_entry_m = Label(root, text="Enter m:", bg='#dccdc7')
        self.label_entry_n = Label(root, text="Enter n:", bg='#dccdc7')
        self.label_entry_m.grid(row=0, column=0, padx=3, pady=3)
        self.label_entry_n.grid(row=1, column=0, padx=3, pady=3)
        self.entry_m.grid(row=0, column=1)
        self.entry_n.grid(row=1, column=1)
        self.btn_start = Button(root, text="Start", command=lambda: self.check(), bg='#dccdc7')
        self.btn_start.grid(row=3, column=0, padx=3, pady=3)
        self.label = Label()

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
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        global n
        n = self.entry_n.get()
        if (n == "") and (show_empty_input == False) and (show_non_digit_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                n = int(n)
                n_correct_input += 1
                if n > 0:
                    n_correct_input += 1
            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        try:
            if int(n) != int(m):
                showwarning("Warning", "To calculate determinate number of rows must be equal to number of columns")
        except ValueError:
            pass

        if m_correct_input == 2 and n_correct_input == 2 and n == m:
            _list = root.winfo_children()

            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())

            for item in _list:
                item.grid_forget()

            self.show()

    def show(self):
        a = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                entry = Entry(root, width=10)
                entry.grid(row=i, column=j, padx=3, pady=3)
                a[i][j] = entry
        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(m, n, a), bg='#dccdc7')
        btn1.grid(row=m + 1, column=0, columnspan=3, padx=3, pady=3)

    def calculate(self, m, n, a):
        c = []
        show_empty_input = False
        show_non_digit_input = False
        b = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                b[i][j] = a[i][j].get()
                if (b[i][j] == "") and (show_empty_input == False) and(show_non_digit_input == False):
                    showwarning("Warning", "You have empty input")
                    show_empty_input = True
                else:
                    try:
                        b[i][j] = float(a[i][j].get())
                        c.append(b[i][j])
                    except ValueError:
                        if (show_non_digit_input == False) and (show_empty_input == False):
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True

        if len(c) == m*n:
            np.array(c)
            c = np.reshape(c, (m, n))
            self.label.grid_forget()
            self.label.configure(text="Matrix determinant = %f" % np.linalg.det(c), bg='#dccdc7')
            self.label.grid(row=m + 2, column=0, columnspan=n, padx=3, pady=3)


class Rank:

    def __init__(self):
        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        for item in _list:
            item.grid_forget()

        root.title("Matrix Rank")

        self.entry_m = Entry(root)
        self.entry_n = Entry(root)
        self.label_entry_m = Label(root, text="Enter m:", bg='#dccdc7')
        self.label_entry_n = Label(root, text="Enter n:", bg='#dccdc7')
        self.label_entry_m.grid(row=0, column=0)
        self.label_entry_n.grid(row=1, column=0)
        self.entry_m.grid(row=0, column=1, padx=3, pady=3)
        self.entry_n.grid(row=1, column=1, padx=3, pady=3)
        self.btn_start = Button(root, text="Start", command=lambda: self.check(), bg='#dccdc7')
        self.btn_start.grid(row=3, column=0, padx=3, pady=3)
        self.label = Label()

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
                if m > 0:
                    m_correct_input = 1

            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        global n
        n = self.entry_n.get()
        if (n == "") & (show_empty_input == False) and (show_non_digit_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                n = int(n)
                if n > 0:
                    n_correct_input = 1
            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        if m_correct_input == 1 and n_correct_input == 1:
            _list = root.winfo_children()

            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())

            for item in _list:
                item.grid_forget()

            self.show()

    def show(self):
        a = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                entry = Entry(root, width=10)
                entry.grid(row=i, column=j, padx=3, pady=3)
                a[i][j] = entry
        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(m, n, a), bg='#dccdc7')
        btn1.grid(row=m + 1, column=0, columnspan=3, padx=3, pady=3)

    def calculate(self, m, n, a):
        c = []
        show_empty_input = False
        show_non_digit_input = False
        b = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                b[i][j] = a[i][j].get()
                if (b[i][j] == "") and (show_empty_input == False) and (show_non_digit_input == False):
                    showwarning("Warning", "You have empty input")
                    show_empty_input = True
                else:
                    try:
                        b[i][j] = float(a[i][j].get())
                        c.append(b[i][j])
                    except ValueError:
                        if (show_non_digit_input == False) and (show_empty_input == False):
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True

        if len(c) == len(a)*len(a[0]):
            np.array(c)
            c = np.reshape(c, (m, n))
            self.label.grid_forget()
            self.label.configure(text="Matrix rank = " + str(np.linalg.matrix_rank(c)), bg='#dccdc7')
            self.label.grid(row=m + 2, column=0, columnspan=n, padx=3, pady=3)


class MatrixSum:

    def __init__(self):
        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        for item in _list:
            item.grid_forget()

        root.title("Matrix Sum")

        self.entry_m = Entry(root)
        self.entry_n = Entry(root)
        self.label_entry_m = Label(root, text="Enter m:", bg='#dccdc7')
        self.label_entry_n = Label(root, text="Enter n:", bg='#dccdc7')
        self.label_entry_m.grid(row=0, column=0, padx=3, pady=3)
        self.label_entry_n.grid(row=1, column=0, padx=3, pady=3)
        self.entry_m.grid(row=0, column=1, padx=3, pady=3)
        self.entry_n.grid(row=1, column=1, padx=3, pady=3)
        self.btn_start = Button(root, text="Start", command=lambda: self.check(), bg='#dccdc7')
        self.btn_start.grid(row=3, column=0, padx=3, pady=3)
        self.label = Label()

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
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        global n
        n = self.entry_n.get()
        if (n == "") & (show_empty_input == False) and (show_non_digit_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                n = int(n)
                n_correct_input += 1
                if n > 0:
                    n_correct_input += 1
            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        if m_correct_input == 2 and n_correct_input == 2:
            _list = root.winfo_children()

            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())

            for item in _list:
                item.grid_forget()

            self.show()

    def show(self):
        a = [[0 for x in range(n)] for y in range(m)]
        c = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                entry1 = Entry(root, width=10)
                entry1.grid(row=i, column=j, padx=3, pady=3)
                label_empty = Label(root, width=5, bg='#dccdc7')
                label_empty.grid(row=i, column=n+1, padx=3, pady=3)
                entry2 = Entry(root, width=10)
                entry2.grid(row=i, column=n+j+2, padx=3, pady=3)
                a[i][j] = entry1
                c[i][j] = entry2
        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(m, n, a, c), bg='#dccdc7')
        btn1.grid(row=m + 1, column=0, columnspan=3, padx=3, pady=3)

    def calculate(self, m, n, a, c):
        show_empty_input = False
        show_non_digit_input = False
        b_count = 0
        d_count = 0
        b = [[0 for x in range(n)] for y in range(m)]
        d = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                b[i][j] = a[i][j].get()
                d[i][j] = c[i][j].get()
                if (b[i][j] == "") & (d[i][j] == "") & (show_empty_input == False) and (show_non_digit_input == False):
                    showwarning("Warning", "You have empty input")
                    show_empty_input = True
                else:
                    try:
                        b[i][j] = float(a[i][j].get())
                        b_count += 1
                        d[i][j] = float(c[i][j].get())
                        d_count += 1
                    except ValueError:
                        if show_non_digit_input == False and show_empty_input == False:
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True

        # for i in range(m):
        #     for j in range(n):
        #         self.label.grid_forget()

        if (b_count == len(a)*len(a[0])) and (d_count == len(c)*len(c[0])):
            for i in range(m):
                for j in range(n):
                    self.label = Label(root, width=3, text=b[i][j] + d[i][j], bg='#dccdc7')
                    self.label.grid(row=i+m+2, column=j, padx=3, pady=3)


class MatrixMultiplication:

    def __init__(self):
        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        for item in _list:
            item.grid_forget()

        root.title("Matrix Multiplication")

        self.entry_m1 = Entry(root)
        self.entry_n1 = Entry(root)
        self.entry_m2 = Entry(root)
        self.entry_n2 = Entry(root)

        self.label_entry_m1 = Label(root, text="Enter m1:", bg='#dccdc7')
        self.label_entry_n1 = Label(root, text="Enter n1:", bg='#dccdc7')
        self.label_entry_m1.grid(row=0, column=0, padx=3, pady=3)
        self.label_entry_n1.grid(row=1, column=0, padx=3, pady=3)
        self.entry_m1.grid(row=0, column=1, padx=3, pady=3)
        self.entry_n1.grid(row=1, column=1, padx=3, pady=3)

        self.label_entry_m2 = Label(root, text="Enter m2:", bg='#dccdc7')
        self.label_entry_n2 = Label(root, text="Enter n2:", bg='#dccdc7')
        self.label_entry_m2.grid(row=0, column=2, padx=3, pady=3)
        self.label_entry_n2.grid(row=1, column=2, padx=3, pady=3)
        self.entry_m2.grid(row=0, column=3, padx=3, pady=3)
        self.entry_n2.grid(row=1, column=3, padx=3, pady=3)

        self.btn_start = Button(root, text="Start", command=lambda: self.check(), bg='#dccdc7')
        self.btn_start.grid(row=3, column=0, padx=3, pady=3)

    def check(self):
        show_empty_input = False
        show_non_digit_input = False
        m1_correct_input = 0
        n1_correct_input = 0
        m2_correct_input = 0
        n2_correct_input = 0

        m1 = self.entry_m1.get()
        if (m1 == "") & (show_empty_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                m1 = int(m1)
                if m1 > 0:
                    m1_correct_input = 1

            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        n1 = self.entry_n1.get()
        if (n1 == "") and (show_empty_input == False) and (show_non_digit_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                n1 = int(n1)
                if n1 > 0:
                    n1_correct_input = 1
            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        m2 = self.entry_m2.get()
        if (m2 == "") and (show_empty_input == False) and (show_non_digit_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                m2 = int(m2)
                if m2 > 0:
                    m2_correct_input = 1

            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        n2 = self.entry_n2.get()
        if (n2 == "") and (show_empty_input == False) and (show_non_digit_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                n2 = int(n2)
                if n2 > 0:
                    n2_correct_input = 1
            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        if m1_correct_input == 1 and n1_correct_input == 1 and m2_correct_input == 1 and n2_correct_input == 1 \
                and n1 == m2:
            _list = root.winfo_children()

            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())

            for item in _list:
                item.grid_forget()

            self.show(m1, n1, m2, n2)

        else:
            if (show_non_digit_input == False) and (show_empty_input == False):
                showwarning("Warning", "Matrix shape are incorrect. Try another one.")

    def show(self, m1, n1, m2, n2):
        a = [[0 for x in range(n1)] for y in range(m1)]
        c = [[0 for x in range(n2)] for y in range(m2)]
        for i in range(m1):
            for j in range(n1):
                entry1 = Entry(root, width=10)
                entry1.grid(row=i+1, column=j, padx=3, pady=3)
                label_empty = Label(root, width=5, bg='#dccdc7')
                label_empty.grid(row=i+1, column=n1+1, padx=3, pady=3)
                # entry2 = Entry(root, width=10)
                # entry2.grid(row=i+1, column=n1+j+2)
                a[i][j] = entry1
                # c[i][j] = entry2

        for i in range(m2):
            for j in range(n2):
                # entry1 = Entry(root, width=10)
                # entry1.grid(row=i+1, column=j)
                # label_empty = Label(root, width=5)
                # label_empty.grid(row=i+1, column=n1+1)
                entry2 = Entry(root, width=10)
                entry2.grid(row=i+1, column=n1+j+2, padx=3, pady=3)
                # a[i][j] = entry1
                c[i][j] = entry2

        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(m1, n1, m2, n2, a, c), bg='#dccdc7')
        btn1.grid(row=m1+1, column=0, padx=3, pady=3)

    def calculate(self, m1, n1, m2, n2, a, c):
        show_empty_input = False
        show_non_digit_input = False
        b_count = 0
        d_count = 0
        b = [[0 for x in range(n1)] for y in range(m1)]
        d = [[0 for x in range(n2)] for y in range(m2)]
        for i in range(m1):
            for j in range(n1):
                b[i][j] = a[i][j].get()
                if (b[i][j] == "") and (show_empty_input == False) and (show_non_digit_input == False):
                    showwarning("Warning", "You have empty input")
                    show_empty_input = True
                else:
                    try:
                        b[i][j] = float(a[i][j].get())
                        b_count += 1
                    except ValueError:
                        if (show_non_digit_input == False) and (show_empty_input == False):
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True

        for i in range(m2):
            for j in range(n2):
                d[i][j] = c[i][j].get()
                if (d[i][j] == "") and (show_empty_input == False) and (show_non_digit_input == False):
                    showwarning("Warning", "You have empty input")
                    show_empty_input = True
                else:
                    try:
                        d[i][j] = float(c[i][j].get())
                        d_count += 1
                    except ValueError:
                        if (show_non_digit_input == False) and (show_empty_input == False):
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True

        if (b_count == len(a)*len(a[0])) and (d_count == len(c)*len(c[0])):
            np.array(b)
            b = np.reshape(b, (m1, n1))

            np.array(d)
            d = np.reshape(d, (m2, n2))

            e = np.dot(b, d)

            for i in range(m1):
                for j in range(n2):
                    label = Label(root, width=3, text=e[i][j], bg='#dccdc7')
                    label.grid(row=m2+i+3, column=j, padx=3, pady=3)
        elif(show_non_digit_input == False) and (show_empty_input == False):
            showwarning("Warning", "Incorrect values")


class MatrixEquation:

    def __init__(self):
        _list = root.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        for item in _list:
            item.grid_forget()

        root.title("Matrix Equation")

        self.entry_m = Entry(root)
        self.entry_n = Entry(root)
        self.label_entry_m = Label(root, text="Enter m:", bg='#dccdc7')
        self.label_entry_n = Label(root, text="Enter n:", bg='#dccdc7')
        self.label_entry_m.grid(row=0, column=0, padx=3, pady=3)
        self.label_entry_n.grid(row=1, column=0, padx=3, pady=3)
        self.entry_m.grid(row=0, column=1, padx=3, pady=3)
        self.entry_n.grid(row=1, column=1, padx=3, pady=3)
        self.btn_start = Button(root, text="Start", command=lambda: self.check(), bg='#dccdc7')
        self.btn_start.grid(row=3, column=0, padx=3, pady=3)
        self.label = Label()

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
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        global n
        n = self.entry_n.get()
        if (n == "") & (show_empty_input == False) and (show_non_digit_input == False):
            showwarning("Warning", "You have empty input")
            show_empty_input = True
        else:
            try:
                n = int(n)
                n_correct_input += 1
                if n > 0:
                    n_correct_input += 1
            except ValueError:
                if show_non_digit_input == False and show_empty_input == False:
                    showwarning("Warning", "Your input include non digit symbols")
                    show_non_digit_input = True

        if m_correct_input == 2 and n_correct_input == 2:
            _list = root.winfo_children()

            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())

            for item in _list:
                item.grid_forget()

            self.show()

    def show(self):
        a = [[0 for x in range(n)] for y in range(m)]
        c = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                label_bracket1 = Label(root, width=1, bg="#dccdc7", text="(", padx=3, pady=3)
                label_bracket1.grid(row=i, column=0, padx=3, pady=3)
                label_bracket2 = Label(root, width=1, bg="#dccdc7", text=")", padx=3, pady=3)
                label_bracket2.grid(row=i, column=n+1, padx=3, pady=3)
                label_x = Label(root, width=5, bg="#dccdc7", text=("x( %d ) = " % (i + 1)), padx=3, pady=3)
                label_x.grid(row=i, column=n+2)

                entry1 = Entry(root, width=10)
                entry1.grid(row=i, column=j+1, padx=3, pady=3)

                label_empty = Label(root, width=5, bg='#dccdc7')
                label_empty.grid(row=i, column=n+3, padx=3, pady=3)
                a[i][j] = entry1

            entry2 = Entry(root, width=10)
            entry2.grid(row=i, column=n + j + 3, padx=3, pady=3)
            c[i] = entry2

        btn1 = Button(root, text="Calculate", command=lambda: self.calculate(a, c), bg='#dccdc7')
        btn1.grid(row=m + 1, column=0, columnspan=3, padx=3, pady=3)

    def calculate(self, a, c):
        show_empty_input = False
        show_non_digit_input = False
        b_count = 0
        d_count = 0
        b = [[0 for x in range(n)] for y in range(m)]
        d = [[0 for x in range(1)] for y in range(m)]
        for i in range(m):

            for j in range(n):
                b[i][j] = a[i][j].get()
                if (b[i][j] == "") and ((show_empty_input == False) and (show_non_digit_input == False)):
                    showwarning("Warning", "You have empty input")
                    show_empty_input = True
                else:
                    try:
                        b[i][j] = float(a[i][j].get())
                        b_count += 1
                    except ValueError:
                        if show_non_digit_input == False and show_empty_input == False:
                            showwarning("Warning", "Your input include non digit symbols")
                            show_non_digit_input = True

            d[i] = c[i].get()
            if (d[i] == "") and ((show_empty_input == False) and (show_non_digit_input == False)):
                showwarning("Warning", "You have empty input")
                show_empty_input = True
            else:
                try:
                    d[i] = float(c[i].get())
                    d_count += 1
                except ValueError:
                    if show_non_digit_input == False and show_empty_input == False:
                        showwarning("Warning", "Your input include non digit symbols")
                        show_non_digit_input = True

        print(b_count, d_count)

        if (b_count == len(a)*len(a[0])) and (d_count == len(c)):
            d = np.array(d)
            b = np.array(b)

            x = np.linalg.solve(b, d)

            label_answer = Label(root, width=7, text=x)
            label_answer.grid(row=0, column=0, padx=3, pady=3)


        # if (b_count == len(a)*len(a[0])) and (d_count == len(c)*len(c[0])):
        #     for i in range(m):
        #         for j in range(n):
        #             self.label = Label(root, width=3, text=b[i][j] + d[i][j], bg='#dccdc7')
        #             self.label.grid(row=i+m+2, column=j, padx=3, pady=3)


if __name__ == "__main__":
    MainScreen()


# https://stackoverflow.com/questions/6178153/how-to-change-menu-background-color-of-tkinters-optionmenu-widget
# зробити меню через OptionMenu (або Menubutton)
# https://effbot.org/tkinterbook/optionmenu.htm
main_menu = Menu(root)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Open", menu=first_item)

first_item.add_command(label="Main Screen", command=MainScreen)
first_item.add_command(label="Matrix Determinant", command=Determinant)
first_item.add_command(label="Matrix Rank", command=Rank)
first_item.add_command(label="Matrix Sum", command=MatrixSum)
first_item.add_command(label="Matrix Multiplication", command=MatrixMultiplication)
first_item.add_command(label="Matrix Equation", command=MatrixEquation)

root.configure(bg='#dccdc7', menu=main_menu, padx=5, pady=5)

root.mainloop()
