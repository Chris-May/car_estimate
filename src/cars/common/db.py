import os
import sqlite3


def sqlite_execute(command, data=None):
    conn = sqlite3.connect(os.getenv('SQLITE_DBNAME'))
    cursor = conn.cursor()
    results = (
        cursor.execute(command, data) if data else cursor.execute(command).fetchall()
    )
    conn.commit()
    conn.close()
    return results
