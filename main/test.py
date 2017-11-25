from tkinter import *
from tkinter import ttk
import time


def run(p):
    p.start()
    total = 1
    for i in range(1, 10001):
        total *= i
    p.stop()
    return total


if __name__ == "__main__":
    parent = Tk()
    label = Label(parent, text="TEST")
    label.pack()

    p = ttk.Progressbar(parent, orient="horizontal", length=200, mode="indeterminate", value=200.0)
    p.pack()

    label = Label(parent, text="x")
    label.pack()

    x = run(p)

    print(x)
    parent.mainloop()