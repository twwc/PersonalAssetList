#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from backend import key_check
from backend import hasher
from frontend.views.assets_view import AssetsView
from frontend.views import financial_assets_view
from frontend.views import license_assets_view
from frontend.views import technology_assets_view
from frontend.views import online_accounts_assets_view


def wrong_key_error():
    messagebox.showerror('Submission Error', 'Incorrect key. Try again')


class AccessView:
    def __init__(self, title, bg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        access_key_frame = Frame(root, bg=bg_color)
        access_key_frame.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(access_key_frame, text='Access Key', font='ELITE 12 bold', bg=bg_color)
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(access_key_frame, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)
        access_key_entry.focus_force()

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
    def __init__(self, title, bg_color, lblframe_text, fg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        access_key_lblframe = LabelFrame(root, bg=bg_color, text=lblframe_text, fg=fg_color, font='ELITE 12 bold')
        access_key_lblframe.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(access_key_lblframe, text='Access Key:', bg=bg_color, font='Elite 10 bold')
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(access_key_lblframe, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)
        access_key_entry.focus_force()

        button_frame = Frame(root, bg=bg_color)
        button_frame.grid(row=1, column=0, pady=5, padx=5)
        submit_button = Button(button_frame, text='SUBMIT', relief='raised', font='ELITE 10 bold', width=10)
        submit_button.grid(row=0, column=0, pady=5, padx=5)

        def init_submit():
            hashed_key = hasher.hash_key(access_key_entry.get())
            if key_check.verify_key(hashed_key) is True:
                root.destroy()
                financial_assets_view.FinancialAssetsView(title='Financial Assets', bg_color=bg_color,
                                                          lbl_text='Financial Asset Submission', lbl_text_color='blue')
            else:
                access_key_entry.delete(0, END)
                wrong_key_error()

        submit_button.configure(command=init_submit)

        root.mainloop()


class TechnologyAccessView:
    def __init__(self, title, bg_color, lblframe_text, fg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        access_key_lblframe = LabelFrame(root, bg=bg_color, fg=fg_color, text=lblframe_text, font='ELITE 12 bold')
        access_key_lblframe.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(access_key_lblframe, bg=bg_color, text='Access Key:', font='ELITE 10 bold')
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(access_key_lblframe, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)
        access_key_entry.focus_force()

        submit_button_frame = Frame(root, bg=bg_color)
        submit_button_frame.grid(row=1, column=0, pady=5, padx=5)
        submit_button = Button(submit_button_frame, text='SUBMIT', relief='raised', width=10, font='ELITE 10 bold')
        submit_button.grid(row=0, column=0, pady=5, padx=5)

        def init_submit():
            hashed_key = hasher.hash_key(access_key_entry.get())
            if key_check.verify_key(hashed_key) is True:
                root.destroy()
                technology_assets_view.TechnologyAssetsView(title='Technology Assets', bg_color=bg_color)
            else:
                access_key_entry.delete(0, END)
                wrong_key_error()

        submit_button.configure(command=init_submit)

        root.mainloop()


class LicenseAccessView:
    def __init__(self, title, bg_color, lblframe_text, fg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        access_key_lblframe = LabelFrame(root, bg=bg_color, text=lblframe_text, fg=fg_color, font='ELITE 12 bold')
        access_key_lblframe.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(access_key_lblframe, text='Access Key:', font='ELITE 10 bold', bg=bg_color)
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(access_key_lblframe, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)
        access_key_entry.focus_force()

        button_frame = Frame(root, bg=bg_color)
        button_frame.grid(row=1, column=0, pady=5, padx=5)
        submit_button = Button(button_frame, text='SUBMIT', width=10, font='ELITE 10 bold')
        submit_button.grid(row=0, column=0, pady=5, padx=5)

        def init_submit():
            hashed_key = hasher.hash_key(access_key_entry.get())
            if key_check.verify_key(hashed_key) is True:
                root.destroy()
                license_assets_view.LicenseAssetsView(title='License Assets', bg_color=bg_color)
            else:
                access_key_entry.delete(0, END)
                wrong_key_error()

        submit_button.configure(command=init_submit)

        root.mainloop()


class OnlineAccountAccessView:
    def __init__(self, title, bg_color, lblframe_text, fg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        access_key_lblframe = LabelFrame(root, bg=bg_color, text=lblframe_text, fg=fg_color, font='ELITE 12 bold')
        access_key_lblframe.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(access_key_lblframe, text='Access Key:', bg=bg_color, font='ELITE 10 bold')
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(access_key_lblframe, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)
        access_key_entry.focus_force()

        submit_button_frame = Frame(root, bg=bg_color)
        submit_button_frame.grid(row=1, column=0, pady=5, padx=5)
        submit_button = Button(submit_button_frame, text='SUBMIT', width=10, font='ELITE 10 bold')
        submit_button.grid(row=0, column=0, pady=5, padx=5)

        def init_submit():
            hashed_key = hasher.hash_key(access_key_entry.get())
            if key_check.verify_key(hashed_key) is True:
                root.destroy()
                online_accounts_assets_view.OnlineAccountsAssetsView(title='Online Accounts', bg_color=bg_color)
            else:
                access_key_entry.delete(0, END)
                wrong_key_error()

        submit_button.configure(command=init_submit)

        root.mainloop()
