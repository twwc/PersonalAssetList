#!/usr/bin/python3

import sqlite3


class KeyStorage:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute('CREATE TABLE IF NOT EXISTS {} (key TEXT)'.format(self.table_name))
        connection.commit()
        connection.close()

    def insert_key(self, key):
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute('INSERT INTO {} VALUES (?)'.format(self.table_name), (key,))
        connection.commit()
        connection.close()

    def check_key_status(self):
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute('SELECT * FROM {}'.format(self.table_name))
        key = curs.fetchall()
        connection.close()
        return key

    def key_verification(self, key=''):
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute('SELECT key FROM {} WHERE key=?'.format(self.table_name), (key,))
        keys = curs.fetchall()
        connection.close()
        for key in keys:
            return '{}'.format(''.join(key))


# create second DB for Assets
# create functions for adding different tables for different assets
# create functions to implement CRUD for each table in Assets DB

class AssetStorage:
    def __init__(self, db_name, finance_table_name, technology_table_name, license_table_name,
                 online_account_table_name):
        self.db_name = db_name
        self.finance_table_name = finance_table_name
        self.technology_table_name = technology_table_name
        self.license_table_name = license_table_name
        self.online_account_table_name = online_account_table_name
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute(
            "CREATE TABLE IF NOT EXISTS {} (bank_name TEXT, a_number INTEGER, r_number INTEGER)".format(
                self.finance_table_name))
        curs.execute('CREATE TABLE IF NOT EXISTS {} (device_type TEXT, model TEXT, mac TEXT, location TEXT)'.format(
            self.technology_table_name))
        curs.execute(
            'CREATE TABLE IF NOT EXISTS {} (license_account TEXT, license_exp TEXT, quantity INTEGER)'.format(
                self.license_table_name))
        curs.execute('CREATE TABLE IF NOT EXISTS {} ()'.format(self.online_account_table_name))
        connection.commit()
        connection.close()

    def insert_finance_data(self, bank_name, a_number, r_number):
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute("INSERT INTO {} VALUES (?,?,?)".format(self.finance_table_name), (bank_name, a_number, r_number))
        connection.commit()
        connection.close()

    def insert_technology_data(self, device_type, model, mac, location):
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute("INSERT INTO {} VALUES (?,?,?,?)".format(self.technology_table_name),
                     (device_type, model, mac, location))
        connection.commit()
        connection.close()

    def insert_license_data(self, license_account, license_exp, quantity):
        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute("INSERT INTO {} VALUES ()".format(self.license_table_name),
                     (license_account, license_exp, quantity))
        connection.commit()
        connection.close()

    def insert_online_account_data(self, ):
        # create value types for online account assets
        # implement those values in SQL execution function

        connection = sqlite3.connect(self.db_name)
        curs = connection.cursor()
        curs.execute("INSERT INTO {} VALUES ()".format(self.online_account_table_name), ())
        connection.commit()
        connection.close()
