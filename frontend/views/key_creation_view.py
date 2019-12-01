#!/usr/bin/python3

from tkinter import *
from frontend.views import introduction_view
from backend import hasher
from backend import key_check


class KeyCreationView:
    def __init__(self, title, bg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)

        key_creation_frame = Frame(root, bg=bg_color)
        key_creation_frame.grid(row=0, column=0, pady=5, padx=5)
        access_key_label = Label(key_creation_frame, text="Access Key:", font='ELITE 12 bold', bg=bg_color)
        access_key_label.grid(row=0, column=0, pady=5, padx=5)
        access_key_entry = Entry(key_creation_frame, show='*', font='bold')
        access_key_entry.grid(row=0, column=1, pady=5, padx=5)

        buttons_frame = Frame(root, bg=bg_color)
        buttons_frame.grid(row=1, column=0)
        submit_button = Button(buttons_frame, text='SUBMIT', font='ELITE 10 bold', relief='raised', width=10)
        submit_button.grid(row=0, column=0, pady=5, padx=5)
        cancel_button = Button(buttons_frame, text='CANCEL', font='ELITE 10 bold', relief='raised', width=10)
        cancel_button.grid(row=0, column=1, pady=5, padx=5)

        def init_submit():
            if key_check.check_key_field(access_key_entry.get()) is True:
                hashed_key = hasher.hash_key(access_key_entry.get())
                if key_check.check_key_exists() is True:
                    introduction_view.key_db.insert_key(hashed_key)
                    access_key_entry.delete(0, END)
                else:
                    access_key_entry.delete(0, END)

        def init_cancel():
            root.destroy()

        submit_button.configure(command=init_submit)
        cancel_button.configure(command=init_cancel)

        root.mainloop()
