#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class TechnologyAssetsView:
    def __init__(self, title, bg_color, lbl_text, lbl_text_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)
        root.resizable(width=False, height=False)

        technology_assets_entry_lblframe = LabelFrame(root, text=lbl_text, bg=bg_color, fg=lbl_text_color,
                                                      font='ELITE 10 bold')
        technology_assets_entry_lblframe.grid(row=0, column=0, pady=5, padx=5)
        device_type_label = Label(technology_assets_entry_lblframe, bg=bg_color, font='ELITE 10 bold',
                                  text='Device Type')
        device_type_label.grid(row=0, column=0, pady=5, padx=5)
        device_type_entry = Entry(technology_assets_entry_lblframe, font='bold')
        device_type_entry.grid(row=0, column=1, pady=5, padx=5)
        model_label = Label(technology_assets_entry_lblframe, bg=bg_color, font='ELITE 10 bold',
                            text='Device Model')
        model_label.grid(row=1, column=0, pady=5, padx=5)
        model_entry = Entry(technology_assets_entry_lblframe, font='bold')
        model_entry.grid(row=1, column=1, pady=5, padx=5)
        mac_label = Label(technology_assets_entry_lblframe, bg=bg_color, font='ELITE 10 bold', text='MAC Address')
        mac_label.grid(row=2, column=0, pady=5, padx=5)
        mac_entry = Entry(technology_assets_entry_lblframe, font='bold')
        mac_entry.grid(row=2, column=1, pady=5, padx=5)
        location_label = Label(technology_assets_entry_lblframe, bg=bg_color, font='ELITE 10 bold', text='Location')
        location_label.grid(row=3, column=0, pady=5, padx=5)
        location_entry = Entry(technology_assets_entry_lblframe, font='bold')
        location_entry.grid(row=3, column=1, pady=5, padx=5)

        entry_buttons_frame = Frame(root, bg=bg_color)
        entry_buttons_frame.grid(row=1, column=0, pady=5, padx=5)
        submit_button = Button(entry_buttons_frame, text='SUBMIT', font='ELITE 10 bold', width=10)
        submit_button.grid(row=0, column=0, pady=5, padx=5)
        cancel_button = Button(entry_buttons_frame, text='CANCEL', font='ELITE 10 bold', width=10)
        cancel_button.grid(row=1, column=0, pady=5, padx=5)

        technology_assets_view_frame = Frame(root, bg=bg_color)
        technology_assets_view_frame.grid(row=2, column=0, pady=5, padx=5)
        technology_view_box = Text(technology_assets_view_frame, font='ELITE 10 bold')
        technology_view_box.grid(row=0, column=0, pady=5, padx=5)

        root.mainloop()
