#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class FinancialAssetsView:
    def __init__(self, title, bg_color, lbl_text, lbl_text_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        financial_assets_entry_lblframe = LabelFrame(root, bg=bg_color, text=lbl_text, fg=lbl_text_color)
        financial_assets_entry_lblframe.grid(row=0, column=0, pady=5, padx=5)
        bank_name_label = Label(financial_assets_entry_lblframe, text='Bank:', bg=bg_color, font='ELITE 10 bold')
        bank_name_label.grid(row=0, column=0, pady=5, padx=5)
        bank_name_entry = Entry(financial_assets_entry_lblframe, font='bold')
        bank_name_entry.grid(row=0, column=1, pady=5, padx=5)
        credit_name_label = Label(financial_assets_entry_lblframe, bg=bg_color, text='Credit Company:',
                                  font='ELITE 10 bold')
        credit_name_label.grid(row=1, column=0, pady=5, padx=5)
        credit_name_entry = Entry(financial_assets_entry_lblframe, font='bold')
        credit_name_entry.grid(row=1, column=1, pady=5, padx=5)

        entry_buttons_frame = Frame(root, bg=bg_color)
        entry_buttons_frame.grid(row=1, column=0, pady=5, padx=5)
        submit_button = Button(entry_buttons_frame, text='SUBMIT', relief='raised', font='ELITE 10 bold', width=10)
        submit_button.grid(row=0, column=0, pady=5, padx=5)
        cancel_button = Button(entry_buttons_frame, text='CANCEL', relief='raised', font='ELITE 10 bold', width=10)
        cancel_button.grid(row=0, column=1, pady=5, padx=5)

        root.mainloop()
