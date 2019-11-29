#!/usr/bin/python3

import hashlib


def hash_key(key):
    hashed = hashlib.sha3_512()
    hashed.update(key.encode())
    salt = hashlib.sha3_256()
    salt.update(key.encode())
    final_key = hashlib.pbkdf2_hmac('sha256', hashed.digest(), salt.digest(), 750000)
    return final_key.hex()
