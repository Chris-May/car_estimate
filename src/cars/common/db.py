import os
import sqlite3


def sqlite_insert(command, data=None):
    conn = sqlite3.connect(os.getenv('SQLITE_DBNAME'))
    cursor = conn.cursor()
    results = cursor.execute(command, data) if data else cursor.execute(command)
    conn.commit()
    conn.close()
    return results


def sqlite_fetch(command, data=None):
    conn = sqlite3.connect(os.getenv('SQLITE_DBNAME'))
    cursor = conn.cursor()
    results = (
        cursor.execute(command, data).fetchall()
        if data
        else cursor.execute(command).fetchall()
    )
    conn.commit()
    conn.close()
    return results
