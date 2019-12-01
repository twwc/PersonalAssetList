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
