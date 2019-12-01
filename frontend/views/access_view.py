#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


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

        root.mainloop()
