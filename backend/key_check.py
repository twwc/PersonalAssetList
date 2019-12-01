#!/usr/bin/python3

from tkinter import messagebox
from tkinter import *
from frontend.views import introduction_view


def check_key_field(secret_key):
    if secret_key == '':
        messagebox.showerror('Key Entry Error', 'Access Key entry must not be empty!')
    elif len(secret_key) < 8:
        messagebox.showerror('Key Error', 'Key must be at least 8 characters in length')
    else:
        return True


def check_key_exists():
    if len(introduction_view.key_db.check_key_status()) >= 1:
        messagebox.showerror('Key Submission Error', 'A key already exists.')
    else:
        return True


def verify_key(secret_key):
    if introduction_view.key_db.key_verification(secret_key):
        return True
