from tkinter import *

# TODO: float numbers , clear last char, brackets, square, power

root = Tk()
root.title("Timer")

text = ''


def calculate(key):
    global text
    if key == "=":
        try:
            text = eval(text)
            text = round(text, 8)
            text = str(text)
        except SyntaxError:
            pass
        except ZeroDivisionError:
            pass
    elif key == "C":
        text = ''
    else:
        text += key
    l1.configure(text=text)
    # a = eval(txt)


l1 = Label(root, width=14, font=("Ubuntu", 20))
l1.grid(columnspan=4)

b1 = Button(root, width=6, heigh=3, text="1", command=lambda: calculate("1"))
b1.grid(row=1, column=0, padx=2, pady=2)
b2 = Button(root, width=6, heigh=3, text="2", command=lambda: calculate("2"))
b2.grid(row=1, column=1, padx=2, pady=2)
b3 = Button(root, width=6, heigh=3, text="3", command=lambda: calculate("3"))
b3.grid(row=1, column=2, padx=2, pady=2)
b_plus = Button(root, width=6, heigh=3, text="+", command=lambda: calculate("+"))
b_plus.grid(row=1, column=3, padx=2, pady=2)

b4 = Button(root, width=6, heigh=3, text="4", command=lambda: calculate("4"))
b4.grid(row=2, column=0, padx=2, pady=2)
b5 = Button(root, width=6, heigh=3, text="5", command=lambda: calculate("5"))
b5.grid(row=2, column=1, padx=2, pady=2)
b6 = Button(root, width=6, heigh=3, text="6", command=lambda: calculate("6"))
b6.grid(row=2, column=2, padx=2, pady=2)
b_minus = Button(root, width=6, heigh=3, text="-", command=lambda: calculate("-"))
b_minus.grid(row=2, column=3, padx=2, pady=2)

b7 = Button(root, width=6, heigh=3, text="7", command=lambda: calculate("7"))
b7.grid(row=3, column=0, padx=2, pady=2)
b8 = Button(root, width=6, heigh=3, text="8", command=lambda: calculate("8"))
b8.grid(row=3, column=1, padx=2, pady=2)
b9 = Button(root, width=6, heigh=3, text="9", command=lambda: calculate("9"))
b9.grid(row=3, column=2, padx=2, pady=2)
b_multiply = Button(root, width=6, heigh=3, text="*", command=lambda: calculate("*"))
b_multiply.grid(row=3, column=3, padx=2, pady=2)

b_divide = Button(root, width=6, heigh=3, text="/", command=lambda: calculate("/"))
b_divide.grid(row=4, column=3)
b_clear = Button(root, width=6, heigh=3, text="C", command=lambda: calculate("C"))
b_clear.grid(row=4, column=2)

b0 = Button(root, heigh=3, width=6, text="0", command=lambda: calculate("0"))
b0.grid(padx=2, pady=2, row=4, column=0)
b_equal = Button(root, heigh=3, width=6, text="=", command=lambda: calculate("="))
b_equal.grid(padx=2, pady=2, row=4, column=1)

root.mainloop()
