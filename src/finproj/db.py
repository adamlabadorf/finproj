"""Code for interfacing with the internal DB of finproj"""

import os
import sqlite3

SQL_SYMBOL_CREATE = '''\
CREATE TABLE symbol (
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    name TEXT
    )

'''

SQL_STOCKS_CREATE = '''\
CREATE TABLE stocks (
    date TEXT,
    symbol TEXT,
    hi REAL,
    low REAL,
    open REAL,
    close REAL,
    volume REAL
    )'''

class FileExistsException(Exception) : pass
class FileNotFoundException(Exception) : pass

globalconn = None

def create(path='~/.local/finproj.db',replace=False) :
    if os.path.exists(path) :
        if not replace :
            raise FileExistsException('path %s already exists and replace == False'%path)
        else :
            os.remove(path)

    full_path = os.path.expanduser(path)
    conn = sqlite3.connect(full_path)

    # cursor
    c = conn.cursor()

    # create tables
    c.execute(SQL_SYMBOL_CREATE)
    c.execute(SQL_STOCKS_CREATE)

    # commit
    conn.commit()
    c.close()

    return conn

def connect(path='~/.local/finproj.db') :
    if not os.path.exists(path) :
        raise FileNotFoundException('path %s does not exist'%path)

    full_path = os.path.expanduser(path)
    conn = sqlite3.connect(full_path)

    return conn

def create_or_connect(path='~/.local/finproj.db',replace=False) :
    try :
        conn = create(path,replace)
    except FileExistsException :
        conn = connect(path)

    return conn
