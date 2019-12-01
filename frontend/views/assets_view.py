#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class AssetsView:
    def __init__(self, title, bg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)

        root.mainloop()
