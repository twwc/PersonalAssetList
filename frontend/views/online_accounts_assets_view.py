#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class OnlineAccountsAssetsView:
    def __init__(self, title, bg_color, lbl_text, lbl_text_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        # add structure
        # refer to 'financial_assets_view' for layout

        online_account_assets_lblframe = LabelFrame(root, text=lbl_text, bg=bg_color, fg=lbl_text_color,
                                                    font='ELITE 10 bold')
        online_account_assets_lblframe.grid(row=0, column=0, pady=5, padx=5)

        # create labels and entries for asset parameters (ex. Account Type, Account Name, Company, etc.)

        root.mainloop()
