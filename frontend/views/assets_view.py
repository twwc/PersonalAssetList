#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from backend import key_check
from frontend.views.financial_assets_view import FinancialAssetsView
from frontend.views.license_assets_view import LicenseAssetsView
from frontend.views.technology_assets_view import TechnologyAssetsView
from frontend.views.online_accounts_assets_view import OnlineAccountsAssetsView


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

        def init_financial_assets():
            FinancialAssetsView(title='Financial Assets', bg_color=bg_color)

        def init_technology_assets():
            if key_check.check_key_exists() is False:
                # display 'access view' window
                # Find a way to have 'access view' take inputs and open correct view without creating different...
                # ...access views for each asset list
                pass
            else:
                TechnologyAssetsView(title='Technology Assets', bg_color=bg_color)

        def init_license_assets():
            if key_check.check_key_exists() is True:
                # display 'access view' window
                # Find a way to have 'access view' take inputs and open correct view without creating different...
                # ...access views for each asset list
                pass
            else:
                LicenseAssetsView(title='License Assets', bg_color=bg_color)

        def init_online_account_assets():
            if key_check.check_key_exists() is True:
                # display 'access view' window
                # Find a way to have 'access view' take inputs and open correct view without creating different...
                # ...access views for each asset list
                pass
            else:
                OnlineAccountsAssetsView(title='Online Accounts Assets', bg_color=bg_color)

        financial_assets_button.configure(command=init_financial_assets)
        technology_assets_button.configure(command=init_technology_assets)
        license_assets_button.configure(command=init_license_assets)
        online_account_assets_button.configure(command=init_online_account_assets)

        root.mainloop()
