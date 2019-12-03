#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from backend import key_check
from backend import hasher
from frontend.views.assets_view import AssetsView


class AccessView:
    def __init__(self, title, bg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)

        access_key_frame = Frame(root, bg=bg_color)
        access_key_frame.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(access_key_frame, text='Access Key', font='ELITE 12 bold', bg=bg_color)
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(access_key_frame, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)

        button_frame = Frame(root, bg=bg_color)
        button_frame.grid(row=1, column=0, pady=5, padx=5)
        access_button = Button(button_frame, text='ACCESS', font='ELITE 10 bold', width=10)
        access_button.grid(row=0, column=0, pady=5, padx=5)

        def init_access():
            hashed_key = hasher.hash_key(access_key_entry.get())
            if key_check.verify_key(hashed_key) is True:
                root.destroy()
                AssetsView(title='Assets', bg_color=bg_color)
            else:
                messagebox.showerror('Access Error', 'Incorrect Key!')

        access_button.configure(command=init_access)

        root.mainloop()


class FinancialAccessView:
    def __init__(self, title, bg_color, fg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)

        access_key_lblframe = LabelFrame(root, bg=bg_color, text='Financial Assets', fg=fg_color)
        access_key_lblframe.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(access_key_lblframe, text='Access Key:', bg=bg_color, font='Elite 10 bold')
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(access_key_lblframe, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)

        button_frame = Frame(root, bg=bg_color)
        button_frame.grid(row=0, column=0, pady=5, padx=5)
        submit_button = Button(button_frame, text='SUBMIT', relief='raised', font='ELITE 10 bold')
        submit_button.grid(row=0, column=0, pady=5, padx=5)

        root.mainloop()
