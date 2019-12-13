#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class LicenseAssetsView:
    def __init__(self, title, bg_color, lbl_text, lbl_text_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        license_assets_lblframe = LabelFrame(root, text=lbl_text, bg=bg_color, fg=lbl_text_color, font='ELITE 10 bold')
        license_assets_lblframe.grid(row=0, column=0, pady=5, padx=5)
        license_account_label = Label(license_assets_lblframe, bg=bg_color, text='License Type', font='ELITE 10 bold')
        license_account_label.grid(row=0, column=0, pady=5, padx=5)
        license_account_entry = Entry(license_assets_lblframe, font='bold')
        license_account_entry.grid(row=0, column=1, pady=5, padx=5)
        license_exp_label = Label(license_assets_lblframe, bg=bg_color)
        license_exp_label.grid(row=1, column=0, pady=5, padx=5)
        license_exp_entry = Entry(license_assets_lblframe)
        license_exp_entry.grid(row=1, column=1, pady=5, padx=5)

        root.mainloop()
