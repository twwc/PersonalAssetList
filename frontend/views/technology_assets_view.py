#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class TechnologyAssetsView:
    def __init__(self, title, bg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        # add structure
        # refer to 'financial_assets_view' for layout

        root.mainloop()
