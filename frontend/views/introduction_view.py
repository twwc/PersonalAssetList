#!/urs/bin/python3

from tkinter import *
from tkinter import messagebox


class IntroductionView:
    def __init__(self, title, bg_color):
        root = Tk()
        root.title(title)
        root.configure(bg=bg_color)

        app_title_frame = Frame(root, bg=bg_color)
        app_title_frame.grid(row=0, column=0, pady=5, padx=5)
        app_title_label = Label(app_title_frame, text='PAL', font='ELITE 20 bold', bg=bg_color)
        app_title_label.grid(row=0, column=0, padx=5)
        extended_app_title_label = Label(app_title_frame, text='Personal Assest List', font='ELITE 10 bold',
                                         bg=bg_color)
        extended_app_title_label.grid(row=1, column=0, padx=5)

        intro_frame = Frame(root, bg=bg_color)
        intro_frame.grid(row=1, column=0, pady=5, padx=5)
        intro_text = Text(intro_frame, width=67, height=29, font='ELITE 11 bold')
        intro_text.grid(row=0, column=0, pady=5, padx=5)
        with open('frontend/views/intro.txt', 'r') as introduction:
            contents = introduction.readlines()
            for lines in contents:
                intro_text.insert(END, lines)
            intro_text.configure(state='disabled')

        button_frame = Frame(root, bg=bg_color)
        button_frame.grid(row=2, column=0, pady=5, padx=5)
        enter_button = Button(button_frame, text='ENTER', font='ELITE 10 bold', width=12)
        enter_button.grid(row=0, column=0, pady=5, padx=5)

        root.mainloop()
