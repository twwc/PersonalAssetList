#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class AssetsView:
    def __init__(self, title, bg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)

        assets_buttons_frame = Frame(root, bg=bg_color)
        assets_buttons_frame.grid(row=0, column=0, pady=5, padx=5)
        financial_assets_button = Button(assets_buttons_frame, width=25, height=15, bg='yellow')
        financial_assets_button.grid(row=0, column=0, pady=5, padx=5)
        technology_assets_button = Button(assets_buttons_frame, width=25, height=15, bg='yellow')
        technology_assets_button.grid(row=0, column=1, pady=5, padx=5)
        license_assets_button = Button(assets_buttons_frame, width=25, height=15, bg='yellow')
        license_assets_button.grid(row=0, column=2, pady=5, padx=5)
        online_account_assets_button = Button(assets_buttons_frame, width=25, height=15, bg='yellow')
        online_account_assets_button.grid(row=0, column=3, pady=5, padx=5)

        # Create backend for key status
        # If key exists ask for key every time an asset button is pressed

        def init_financial_assets():
            # Check for key
            # if key exists display access key window
            # else just display financial window
            pass

        def init_technology_assets():
            # check for key
            # if key exists display access key window
            # else display technology window
            pass

        def init_license_assets():
            # check for key
            # if key exists display access key window
            # else display license window
            pass

        def init_online_account_assets():
            # check for key
            # if key exists display access key window
            # else display online accounts window
            pass

        root.mainloop()
