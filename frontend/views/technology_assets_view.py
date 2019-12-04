#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class TechnologyAssetsView:
    def __init__(self, title, bg_color, lbl_text, lbl_text_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        # add structure
        # refer to 'financial_assets_view' for layout

        technology_assets_entry_lblframe = LabelFrame(root, text=lbl_text, bg=bg_color, fg=lbl_text_color,
                                                      font='ELITE 10 bold')
        technology_assets_entry_lblframe.grid(row=0, column=0, pady=5, padx=5)

        # create labels and entries for asset parameters (ex. device type, MAC, OS, IP, etc.)

        root.mainloop()
