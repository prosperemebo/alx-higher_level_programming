#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_name = argv[3]
    db_user = argv[1]
    db_password = argv[2]

    db = MySQLdb.connect(
        host="localhost",
        user=db_user,
        password=db_password,
        database=db_name,
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    result = cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    db.close()
